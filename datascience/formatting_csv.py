import csv
import os

new_format = []
INPUT_DIR = r"C:\Users\Tony\Desktop\notpat"
for filename in os.listdir(INPUT_DIR):
    with open(os.path.join(INPUT_DIR,filename), 'r+', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            new_format.append(row[0])
print(new_format)


with open('Formated.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for row in new_format:
        wr.writerow([row])