from PIL import Image
import pytesseract

def ocr_tesseract():
    # Image_file = "temp.png"
    Image_file = "test.jpeg"
    im = Image.open(Image_file)
    text = pytesseract.image_to_string(im)

    print(text)

if __name__ == '__main__':
    ocr_tesseract()
