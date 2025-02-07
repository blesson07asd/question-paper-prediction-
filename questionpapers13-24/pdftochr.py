import cv2
import pytesseract

pdf= "C:\Users\LENOVO\Desktop\question paper prediction\question-paper-prediction-\questionpapers13-24\mergedpdf.pdf"
def ocr_core(pdf):
    text = pytesseract.image_to_string(pdf)
    return text
def removenoise(pdf):
    return cv2.medianBlur(pdf,5)
def grayscale(pdf):
    return cv2.cvtColor(pdf, cv2.COLOR_BGR2GRAY)
def thresholding(pdf):
    return cv2.threshold(pdf, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

pdf=grayscale(pdf)
pdf=thresholding(pdf)
pdf=removenoise(pdf)

print(ocr_core(pdf))