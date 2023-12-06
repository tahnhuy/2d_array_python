import sys
from random import randint

def inputValue(list, rows, cols):
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            value = randint(0, 51)
            row.append(value)
        list.append(row)

    return list

def printValue(list):
    for row in list:
        print(' '.join(map(str, row)))

def findMin(list, rows, cols):
    minValue = list[0][0]
    for i in range(0, rows):
        for j in range(0, cols):
            if list[i][j] < minValue:
                minValue = list[i][j]

    return minValue

def sumAll(list, rows, cols):
    sum = 0
    for i in range(0, rows):
        for j in range(0, cols):
            sum += list[i][j]

    return sum

def countAppearanceX(list, rows, cols):
    x = int(input("Enter value of x: "))
    count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if list[i][j] == x:
                count += 1
    
    return count

def countAppearance(list, rows, cols):
    a = []
    aSize = 0
    position = 0
    count = 1
    for i in range(0, rows):
        for j in range(0, cols):
            a.append(list[i][j])
            aSize += 1
    
    a.sort()

    while position < aSize:
        for i in range(0, aSize - 1):
            if a[i] == a[position] and a[i] == a[i + 1]:
                position += 1
                count += 1
        print(f"{a[position]} appears {count} times")
        position += 1
        count = 1

def findMaxPostion(list, rows, cols):
    max = -sys.maxsize - 1
    row = 0
    col = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if list[i][j] > max:
                max = list[i][j]
                row = i
                col = j

    return row, col;

def findMaxRow(list ,rows ,cols):
    max = -sys.maxsize - 1
    posMax = 0
    for i in range(0, rows):
        sum = 0
        for j in range(0, cols):
            sum += list[i][j]
        
        if sum > max:
            max = sum
            posMax = i 

    maxRow = []
    sum = 0
    for i in range(0, cols):
        maxRow.append(list[posMax][i])
        sum += list[posMax][i]

    return maxRow, sum, posMax

def findMinCol(list, rows, cols):
    min = sys.maxsize
    posMin = 0
    for i in range(0, cols):
        sum = 0
        for j in range(0, rows):
            sum += list[j][i]

        if sum < min:
            min = sum
            posMin = i
    
    sum = 0
    minCol = []
    for i in range(0, rows):
        minCol.append(list[i][posMin])
        sum += list[i][posMin]
    
    return minCol, sum, posMin

def parallel(list, rows, cols, k):
    list1 = []
    for i in range(0, rows):
        for j in range(0, cols):
            if k == j - i:
                list1.append(list[i][j])
    
    list2 = []
    for i in range(0, rows):
        for j in range(0, cols):
            if k == i - j:
                list2.append(list[i][j])

    return list1, list2

list = []

rows = int(input("Enter numbers of rows: "))
cols = int(input("Enter numbers of columns: "))

inputValue(list, rows, cols)
printValue(list)

print(f"Min value = {findMin(list, rows, cols)}")
print(f"Sum = {sumAll(list, rows, cols)}")
print(f"x appears {countAppearanceX(list, rows, cols)} times")
countAppearance(list, rows, cols)

positionRow, positionCol = findMaxPostion(list, rows, cols)
print(f"Max positon a[{positionRow}][{positionCol}]")

valuesMaxRow, sumMaxRow, positionMaxRow = findMaxRow(list, rows, cols)
print(valuesMaxRow)
print(f"sum max row = {sumMaxRow} at postion {positionMaxRow}")

valuesMinCol, sumMinCol, positionMinCol = findMinCol(list, rows, cols) 
print(valuesMinCol)
print(f"sum min col = {sumMinCol} at position {positionMinCol}")

k = int(input(" k = "))
list1, list2 = parallel(list, rows, cols, k)
print(' '.join(map(str, list1)))
print(' '.join(map(str, list2)))