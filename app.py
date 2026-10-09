
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pypdf import PdfReader
from pptx import Presentation
from docx import Document

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "pptx", "docx", "txt"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def extract_text(path, extension):
    if extension == "pdf":
        reader = PdfReader(path)
        pages = []

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                pages.append(
                    f"[Page {page_number}]\n{text.strip()}"
                )

        return "\n\n".join(pages)

    if extension == "pptx":
        presentation = Presentation(path)
        slides = []

        for slide_number, slide in enumerate(presentation.slides, start=1):
            slide_text = [
                shape.text.strip()
                for shape in slide.shapes
                if shape.has_text_frame and shape.text.strip()
            ]

            if slide_text:
                slides.append(
                    f"[Slide {slide_number}]\n"
                    + "\n".join(slide_text)
                )

        return "\n\n".join(slides)

    if extension == "docx":
        document = Document(path)
        paragraphs = [
            paragraph.text.strip()
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]
        return "\n".join(paragraphs)

    if extension == "txt":
        with open(path, "r", encoding="utf-8-sig") as file:
            return file.read()

    return ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")

    if not file or not file.filename:
        return render_template(
            "index.html",
            message="Please select a file first.",
            message_type="error"
        )

    if not allowed_file(file.filename):
        return render_template(
            "index.html",
            message="Upload a PDF, PPTX, DOCX or TXT file.",
            message_type="error"
        )

    filename = secure_filename(file.filename)

    if not filename:
        return render_template(
            "index.html",
            message="Invalid filename.",
            message_type="error"
        )

    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    try:
        extension = filename.rsplit(".", 1)[1].lower()
        extracted_text = extract_text(path, extension)

        if not extracted_text.strip():
            return render_template(
                "index.html",
                message=(
                    "File uploaded, but no readable text was found. "
                    "Scanned PDFs may require OCR."
                ),
                message_type="error"
            )

        preview = extracted_text[:12000]

        return render_template(
            "index.html",
            message=f"{filename} processed successfully!",
            message_type="success",
            extracted_text=preview,
            character_count=len(extracted_text),
            uploaded_filename=filename
        )

    except Exception as error:
        app.logger.exception("Document processing failed")
        return render_template(
            "index.html",
            message=(
                "The file was uploaded, but its text could not be "
                "extracted. Check the file format and try again."
            ),
            message_type="error"
        )


@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        message="File is too large. Maximum size is 50 MB.",
        message_type="error"
    ), 413


if __name__ == "__main__":
    app.run(debug=True)
