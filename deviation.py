import csv
import math

with open("data.csv", newline="") as f:
    data = csv.reader(f)
    data2 = list(data)

data3 = data2[0]

#print(data)
print(data2)
print(data3)

total = 0
totalEntries = len(data3)

for i in data3:
    total = total + int(i)

mean = total / totalEntries
print(total)
print(totalEntries)
print(mean)