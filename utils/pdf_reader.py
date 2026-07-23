import fitz  # PyMuPDF


def extract_text(uploaded_file):
    """
    Extract all text from an uploaded PDF file.
    """

    text = ""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text