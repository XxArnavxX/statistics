from collections import Counter
import csv 
with open('SOCR.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
#print(fileData)
height = []
for i in range(len(fileData)):
    num = fileData[i][1]
    height.append(float(num))

data = Counter(height)
#print(data)
dataRange = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

    