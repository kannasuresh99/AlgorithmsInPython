import math

a = [90, -9, -87, 22, 53, 0, 2, -32, 88, 101]
b = []
k = 0
for x in range(0, len(a)):
    for i in range(0, len(a)):
        if i < (len(a)-2) and a[i] > a[i+1]:
            tempVariable = a[i]
            a[i] = a[i+1]
            a[i+1] = tempVariable
print(a)
