import io
import os


class ExtractionError(Exception):
    pass


def extract_text(filename, file_bytes):
    """
    Extract text from uploaded TXT or PDF resume.
    """

    try:
        extension = os.path.splitext(filename)[1].lower()

        # TXT file
        if extension == ".txt":
            return file_bytes.decode("utf-8")

        # PDF file
        elif extension == ".pdf":
            try:
                from pypdf import PdfReader
            except ImportError:
                raise ExtractionError(
                    "PDF support requires pypdf. Run: pip install pypdf"
                )

            pdf_file = io.BytesIO(file_bytes)
            reader = PdfReader(pdf_file)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            if not text.strip():
                raise ExtractionError(
                    "Could not extract text from the PDF."
                )

            return text.strip()

        else:
            raise ExtractionError(
                "Only .pdf and .txt files are supported."
            )

    except UnicodeDecodeError:
        raise ExtractionError(
            "Could not read the TXT file. Please use a UTF-8 encoded file."
        )

    except ExtractionError:
        raise

    except Exception as e:
        raise ExtractionError(
            f"Error extracting resume text is: {e}"
        )