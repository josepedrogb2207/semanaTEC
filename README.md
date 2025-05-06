# Deteccion de placas

Este proyecto permite detectar el texto de placas en imágenes usando procesamiento de imagen con OpenCV y reconocimiento óptico de caracteres (OCR) con Tesseract.

## Requisitos

Tener python

Este proyecto utiliza las siguientes librerías:

- `opencv-python`
- `pytesseract`
- `numpy`
- `google.colab` (si se ejecuta en Google Colab)

## Instalación

### 1. Instalar dependencias

```bash
pip install opencv-python pytesseract numpy
```

### 2. Instalar Tesseract OCR

#### En Windows:

1. Descarga el instalador desde: https://github.com/tesseract-ocr/tesseract/wiki
2. Instálalo y agrega la ruta a `tesseract.exe` al `PATH`.
3. También puedes especificar la ruta manualmente en tu script de Python:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### En Google Colab:

Tesseract ya está instalado, solo necesitas importar y ejecutar el código.

## Uso

1. Coloca tu imagen (por ejemplo, `placa_4.jpg`) en el mismo directorio que el script.
2. Ejecuta el script `main.py` (o el nombre que le hayas dado).
3. El sistema mostrará el procesamiento paso a paso y finalmente imprimirá el texto detectado.

## Código principal

El script realiza los siguientes pasos:

- Carga la imagen.
- Convierte a escala de grises.
- Aplica desenfoque gaussiano.
- Detecta bordes con Canny.
- Ejecuta OCR sobre la imagen desenfocada.
- Muestra el texto detectado.

## Ejemplo de salida

```
Imagen en escala de grises: [ventana emergente]
Después de aplicar desenfoque Gaussiano: [ventana emergente]
Bordes detectados con Canny: [ventana emergente]
Texto detectado:
ABC1234
```