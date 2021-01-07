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

height.sort()
number = len(height)
if number % 2==0:
    number1 = float(height[number//2])
    number2 = float(height[number//2-1])
    median = (number1 + number2)/2

else:
    median = height[number//2]

print("the median is: " + str(median))