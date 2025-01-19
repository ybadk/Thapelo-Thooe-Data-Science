
numberList = [12, 11, 55, 23, 6, 78, 33, 4]

max = numberList[0]

for num in numberList:
    if max < num:
        max = num
print(max)
