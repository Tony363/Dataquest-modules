# import PyPDF2

# pdf = open(r"/home/tony/Downloads/Syllabus12.pdf","rb")

# pdfReader = PyPDF2.PdfFileReader(pdf)

# print(f"No. of Pages :{pdfReader.numPages}")

# page_1 = pdfReader.getPage(0)
# print(page_1.extractText())

# pdf.close()

####################################

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import csv
import os

pages = convert_from_path(r"/home/tony/Downloads/Syllabus.pdf",500)

db = []
for i,page in enumerate(pages):
    filename = f"out_{i}.jpg"
    page.save(filename,'JPEG')
    image_out = Image.open(filename)
    text = pytesseract.image_to_string(image_out,lang='eng')
    db.append(text)
    os.remove(filename)
    
with open('syllabus.txt',"w") as f:
    for page in db:
        f.write(page)

################################################################
