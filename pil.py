from PIL import Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

imagem = cv2.imread("i.png")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

im = Image.open("i.png")

text = pytesseract.image_to_string(imagem, lang = 'eng')

print(text)

