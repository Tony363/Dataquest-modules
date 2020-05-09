import textract
import csv 

text = textract.process('/home/tony/Downloads/Syllabus12.pdf')

print(text.decode('utf-8'))
# print(text)



with open('syllabus12.txt',"w") as f:
    f.write(text.decode('utf-8'))
        

    


