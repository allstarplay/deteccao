import pytesseract
import cv2

imagem = cv2.imread(r'C:\Users\george\Desktop\nanascreen\deteccao\i.png')

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem, lang="eng")
print(texto)