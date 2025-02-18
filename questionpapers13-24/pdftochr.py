import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

pdf_text = extract_text_from_pdf(r'C:\Users\LENOVO\Desktop\Question paper pre\question-paper-prediction-\questionpapers13-24\.venv\2019.pdf')
print(pdf_text)
