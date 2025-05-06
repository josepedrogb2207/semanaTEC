# -*- coding: utf-8 -*-

import cv2
import pytesseract
import numpy as np

# Ruta de la imagen
image_path = 'placa_4.jpg'
image = cv2.imread(image_path)

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque Gaussiano
blurred_image = cv2.GaussianBlur(gray_image, (11, 11), 0)

# Detectar bordes con Canny
edges = cv2.Canny(blurred_image, 100, 200)

# Mostrar imágenes procesadas
cv2.imshow("Imagen en escala de grises", gray_image)
cv2.imshow("Después de aplicar desenfoque Gaussiano", blurred_image)
cv2.imshow("Bordes detectados con Canny", edges)

# Esperar a que se presione una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicar OCR sobre la imagen desenfocada
text = pytesseract.image_to_string(blurred_image, config='--psm 8')

# Mostrar texto detectado
print("Texto detectado:")
print(text.strip())