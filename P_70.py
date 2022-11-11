# pip install pytesseract
import pytesseract
from PIL import Image
location = ["x=1,y=1", "x=2,y=1", "x=3,y=1", "x=4,y=1", "x=5,y=1", "x=6,y=1", 'x=7,y=1']
im_01 = Image.open("B.png")
custom_config = r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
numbers_string_01 = pytesseract.image_to_string(im_01, config=custom_config)
x_01 = numbers_string_01.replace("\n\n", ",")
x_01 = x_01[0:len(x_01)-1]
x_01 = x_01.split(',')
for i, name in enumerate(x_01):
    print(f"Location of {name} is: [{location[i]}]")
