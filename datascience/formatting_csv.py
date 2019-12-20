
import csv
import os



new_format = []

INPUT_DIR = r"C:\Users\Tony\Desktop\stock market data\new york"

for filename in os.listdir(INPUT_DIR):

    with open(os.path.join(INPUT_DIR,filename), 'r+', encoding= 'utf-8-sig') as infile:#encoding='utf-8'
        
        head = csv.reader(infile)

        for row in head:
            # if 'ï»¿' in row:
            #     continue
            new_format.append(row)

print(new_format)


with open('Formated.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for row in new_format:
        wr.writerow(row)