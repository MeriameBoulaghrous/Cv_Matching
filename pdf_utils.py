# pdf_utils.py

import PyPDF2

def extract_text_from_pdf(pdf_file):
    print("Extracting text from the PDF file...")
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page_num, page in enumerate(reader.pages):
        print(f"Processing page {page_num + 1}...")
        page_text = page.extract_text()
        if page_text:
            text += page_text
    print("Text extraction from PDF completed.")
    return text
