import csv
import math

with open("data.csv", newline = "") as f:
   reader = csv.reader(f)
   file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    return mean

square = []

for num in data:
    a = int(num) - mean(data)
    a = a**2
    square.append(a)

sum = 0
for x in square:
    sum = sum + x

result = sum/(len(data) - 1)

standarddeviation = math.sqrt(result)

print(standarddeviation)



































