import csv
import pandas
import math

with open("__.csv",newline="") as f:
    reader=csv.reader(f)
    data=list(reader)

##data=[60,61,65,63,98,99,90,95,91,96]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)

    mean=total/n
    return mean

squared_list=[]
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)

sum=0

for i in squared_list:
    sum=sum+i

result=sum/(len(data))
print(result)
stdev=math.sqrt(result)
print(stdev)