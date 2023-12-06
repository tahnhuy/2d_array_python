from random import randint

def inputValue(list, rows, cols):
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(randint(0, 50))
        list.append(row)

    return list

def findMax(list, rows, cols):
    maxValue = list[0][0]

    for i in range(0, rows):
        for j in range(0, cols):
            if list[i][j] > maxValue:
                maxValue = list[i][j]

    return maxValue

def findMin(list, rows, cols):
    minValue = list[0][0]

    for i in range(0, rows):
        for j in range(0, cols):
            if list[i][j] < minValue:
                minValue = list[i][j]

    return minValue

list = []
rows = int(input("Enter numbers of rows: "))
cols = int(input("Enter numbers of columns: "))

inputValue(list, rows, cols)

for row in list:
    print(row)

print(f"Max value  = {findMax(list, rows, cols)}")
print(f"Min value = {findMin(list, rows, cols)}")