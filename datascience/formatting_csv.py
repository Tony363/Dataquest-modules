
import csv
import os



new_format = []

INPUT_DIR = r"C:\Users\Tony\Desktop\github\xgboost-with-raymond\excel"

for filename in os.listdir(INPUT_DIR):

    with open(os.path.join(INPUT_DIR,filename), 'r+') as infile:#encoding='utf-8'
        
        head = csv.reader(infile)

        for row in head:
            if 'ï»¿' in row:
                continue
            new_format.append(row[0])

print(new_format)


with open('Formated.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for row in new_format:
        wr.writerow([row])