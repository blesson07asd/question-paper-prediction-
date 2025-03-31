import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            
            text += reader.pages[page].extract_text()
    return text
def get_sentences_starting_with_numbers(text):
    # Regex pattern to match sentences starting with numbers
    pattern = r'\b\d[\d\s,]*[.!?]'  # This matches a number at the beginning of the sentence, followed by any number of digits or spaces, ending with punctuation.
    sentences = re.findall(pattern, text)
    return sentences

pdf_text = extract_text_from_pdf(r'C:\Users\LENOVO\Desktop\Question paper pre\question-paper-prediction-\questionpapers13-24\.venv\2019.pdf')
print(pdf_text)
print(get_sentences_starting_with_numbers(pdf_text))