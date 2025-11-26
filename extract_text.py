import fitz  
import docx


def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def extract_text(file):
    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(file.read())
        return extract_text_from_pdf("temp.pdf")

    elif file_name.endswith(".docx"):
        with open("temp.docx", "wb") as f:
            f.write(file.read())
        return extract_text_from_docx("temp.docx")

    else:
        return "Unsupported file format"
