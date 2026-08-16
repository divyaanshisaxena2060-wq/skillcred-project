import os
import logging

from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

from extraction import extract_text, ExtractionError
from gemini_client import resume_text_to_portfolio_data, GenerationError
from template import build_portfolio_html

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("portfolio-generator")

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB upload limit

allowed_origins = os.environ.get("ALLOWED_ORIGINS", "*")
origins = "*" if allowed_origins == "*" else [o.strip() for o in allowed_origins.split(",")]
CORS(app, resources={r"/api/*": {"origins": origins}})

@app.get("/")
def home():
    return send_from_directory(".", "index.html")
ALLOWED_EXTENSIONS = (".pdf", ".txt")


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "gemini_key_configured": bool(os.environ.get("GEMINI_API_KEY"))})


@app.post("/api/generate")
def generate_portfolio():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded. Send it as multipart form field 'resume'."}), 400

    file = request.files["resume"]
    filename = file.filename or ""

    if not filename.lower().endswith(ALLOWED_EXTENSIONS):
        return jsonify({"error": "Only .pdf and .txt files are supported."}), 400

    file_bytes = file.read()
    if not file_bytes:
        return jsonify({"error": "Uploaded file is empty."}), 400

    # 1. Extract raw text from the resume
    try:
        resume_text = extract_text(filename, file_bytes)
    except ExtractionError as exc:
        logger.warning("Extraction failed for %s: %s", filename, exc)
        return jsonify({"error": str(exc)}), 422

    # 2. Ask Gemini to turn it into structured portfolio data
    try:
        portfolio_data = resume_text_to_portfolio_data(resume_text)
    except GenerationError as exc:
        logger.error("Gemini generation failed: %s", exc)
        return jsonify({"error": str(exc)}), 502

    # 3. Render the structured data into a self-contained HTML portfolio
    html = build_portfolio_html(portfolio_data)

    return Response(
        html,
        mimetype="text/html",
        headers={"Content-Disposition": "attachment; filename=portfolio.html"},
    )


@app.errorhandler(413)
def too_large(_e):
    return jsonify({"error": "File is too large. Max size is 10 MB."}), 413


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
