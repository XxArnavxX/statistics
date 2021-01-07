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

#print(height)
number = len(height)
total = 0
for x in height:
    total = total + x

mean = total/number
print("mean of the height is: " + str (mean))