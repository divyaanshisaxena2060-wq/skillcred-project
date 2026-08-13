# AI Portfolio Generator

Upload a resume (PDF or TXT), and this app uses Google's Gemini API to extract your
details and generate a self-contained, downloadable HTML portfolio page.

## How it works

1. You upload a resume through the web UI (`index.html`).
2. The Flask backend (`app.py`) extracts raw text from the file (`extraction.py`,
   using `pypdf` for PDFs).
3. That text is sent to Gemini (`gemini_client.py`), which returns structured
   portfolio data as JSON (name, about, skills, education, projects, experience,
   certifications, contact info, social links).
4. The structured data is rendered into a polished, standalone HTML file
   (`template.py`) and returned to you as a download (`portfolio.html`).

## Project structure

```
.
├── app.py                          # Flask app & API routes
├── extraction.py                   # Resume text extraction (PDF/TXT)
├── gemini_client.py                # Gemini API integration
├── template.py                     # Builds the final portfolio HTML
├── index.html                      # Frontend UI (upload form)
├── sample_portfolio_preview.html   # Example of generated output
├── requirements.txt
└── .env                            # Your local config (not committed)
```

## Requirements

- Python 3.9+
- A Google Gemini API key ([Google AI Studio](https://aistudio.google.com/apikey))

## Setup

1. **Clone/unzip the project and install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables.** Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   PORT=5000
   ALLOWED_ORIGINS=*
   ```

   - `GEMINI_API_KEY` — **required**. The app will not start without it.
   - `PORT` — optional, defaults to `5000`.
   - `ALLOWED_ORIGINS` — optional, comma-separated list of allowed CORS origins
     for `/api/*` routes. Defaults to `*` (all origins).

   > ⚠️ **Never commit your `.env` file.** If a key has ever been shared or
   > exposed, rotate it immediately in Google AI Studio.

3. **Run the app:**

   ```bash
   python app.py
   ```

   The app will be available at `http://localhost:5000`.

## API Endpoints

| Method | Endpoint        | Description                                              |
|--------|-----------------|------------------------------------------------------------|
| GET    | `/`             | Serves the frontend (`index.html`)                        |
| GET    | `/api/health`   | Health check; reports whether `GEMINI_API_KEY` is set     |
| POST   | `/api/generate` | Accepts a resume upload, returns generated `portfolio.html` |

### `POST /api/generate`

- **Request:** `multipart/form-data` with a file field named `resume`
  (`.pdf` or `.txt`, max 10 MB).
- **Response:** an HTML file (`portfolio.html`) returned as an attachment.
- **Errors:**
  - `400` – no file, empty file, or unsupported file type
  - `422` – text extraction failed (e.g. unreadable/scanned PDF)
  - `502` – Gemini generation failed or returned invalid data
  - `413` – file exceeds the 10 MB limit

Example with `curl`:

```bash
curl -X POST http://localhost:5000/api/generate \
  -F "resume=@/path/to/resume.pdf" \
  -o portfolio.html
```

## Notes & limitations

- Only `.pdf` and `.txt` resumes are supported.
- Scanned/image-only PDFs with no extractable text will fail extraction.
- The app currently runs with Flask's built-in dev server and `debug=True` —
  use a production WSGI server (e.g. Gunicorn) and disable debug mode before
  deploying publicly.
- Gemini output is only as accurate as the resume text provided; the model is
  instructed not to invent information, but review the generated portfolio
  before sharing it.



