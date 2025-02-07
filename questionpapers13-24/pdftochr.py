from pdf2image import convert_from_path
import cv2
import pytesseract
import numpy as np

pdf_path = r"C:\Users\LENOVO\Desktop\Question paper pre\question-paper-prediction-\questionpapers13-24\mergedpdf.pdf"

# Convert PDF to image
def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    image = images[0]  # Use the first page (you can loop through if needed)
    return np.array(image)

# OCR core function
def ocr_core(image):
    text = pytesseract.image_to_string(image)
    return text

# Remove noise from the image
def removenoise(image):
    return cv2.medianBlur(image, 5)

# Convert the image to grayscale
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to enhance text visibility
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Convert PDF to image
image = pdf_to_image(pdf_path)

# Apply preprocessing
image = grayscale(image)
image = thresholding(image)
image = removenoise(image)

# Use OCR to extract text
extracted_text = ocr_core(image)

print(extracted_text)