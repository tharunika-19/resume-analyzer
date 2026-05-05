import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Test it with any PDF on your computer
pdf_path = r"C:\Users\DELL\Downloads\Tharunika_Bodasu_Resume.pdf"  # change to your PDF path
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)