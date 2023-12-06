from random import randint
import math
import copy

def inputValue(list, level):
    for i in range(level):
        row = []
        for j in range(level):
            row.append(randint(1, 9))
        list.append(row)
    
    return list

def printValue(list, level):
    for row in range(level):
        for col in range(level):
            print(list[row][col], end=" ")
        print()

#a
def upperTriangular(list, level):
    temp = []
    for i in range(level):
        tempRow = []
        for j in range(i+1):
            tempRow.append(" ")

        for j in range(i + 1, level):
            tempRow.append(list[i][j])    
        temp.append(tempRow)

    return temp

#b       
def lowerTriangular(list, level):
    temp = []
    for i in range(1, level):
        tempRow = []
        for j in range(0, i):
            tempRow.append(list[i][j])
        temp.append(tempRow)
    
    return temp

#c
def identityTriangular(level):
    temp = []
    for i in range(level):
        row = []
        for j in range(level):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        temp.append(row)
    
    return temp

#d
def symmetricMatrix(level):
    temp = [[0 for _ in range(level)] for _ in range(level)]

    for i in range(level):
        for j in range(i + 1):
            temp[i][j] = temp[j][i] = randint(10, 99)
    
    return temp 

#e
def sumUpperTriangular(list, level):
    sum = 0
    for i in range(level - 1):
        for j in range(i + 1, level):
            sum += list[i][j]
    
    return sum

#f
def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False

    return True

def sumPrime(list, level):
    sum = 0
    k = int(input("Enter line k = "))
    for i in range(level):
        if isPrime(list[k][i]):
            sum += list[k][i]
    
    return sum

#g
def delLineK(list):
    temp = copy.deepcopy(list)
    k = int(input("Enter line k = "))
    del temp[k]

    return temp

#h
def delColumnK(list):
    temp = copy.deepcopy(list)
    k = int(input("Enter column k = "))
    for row in temp:
        del row[k]

    return temp

#i 
def insertLineK(list, level):
    temp = []
    result = copy.deepcopy(list)
    k = int(input("Enter line k = "))
    for i in range(level):
        value = randint(1, 9)
        temp.append(value)

    result.insert(k, temp)

    return result

#j
def swapRow(list, level):
    position = []
    result = []
    sumRow = []
    sum = 0
    for i in range(level):
        position.append(i)
        for j in range(level):
            sum += list[i][j]
        sumRow.append(sum)
        sum = 0

    for i in range(level - 1):
        for j in range(level - i - 1):
            if sumRow[j] < sumRow[j + 1]:
                temp1 = sumRow[j]
                sumRow[j] = sumRow[j + 1]
                sumRow[j + 1] = temp1

                temp = position[j]
                position[j] = position[j + 1]
                position[j + 1] = temp
    
    for i in range(level):
        row = []
        for j in range(level):
            value = list[position[i]][j]
            row.append(value)
        result.append(row)
    
    return result

#k
def deleteMax(list, level):
    temp = copy.deepcopy(list)
    maxValue = list[0][0]
    positionRow = 0
    positionCol = 0
    for i in range(level):
        for j in range(level):
            if list[i][j] > maxValue:
                maxValue = temp[i][j]
                positionRow = i
                positionCol = j
    
    del temp[positionRow]
    for row in temp:
        del row[positionCol]

    return temp

#l
def findRowPrime(list, level):
    count = 0
    max = 0
    primeRow = 0
    for i in range(level):
        for j in range(level):
            if isPrime(list[j][i]):
                count += 1
        if count > max:
            max = count
            primeRow = i
        count = 0

    return primeRow

def deletePrimeCol(list, level):
    temp = copy.deepcopy(list)
    for row in temp:
        del row[findRowPrime(list, level)]
    
    return temp

def main():
    list = []

    level = int(input('Level = '))
    inputValue(list, level)

    printValue(list, level)
    print()
    print("a.")
    printValue(upperTriangular(list, level), level)

    print()
    print("b.")
    for i in range(0, level - 1):
        for j in range(i + 1):
            print(lowerTriangular(list, level)[i][j], end=" ")
        print()

    print()
    print("c.")
    printValue(identityTriangular(level), level)\

    print()
    print("d.")
    printValue(symmetricMatrix(level), level)

    print()
    print("e.")
    print(f"Sum of upper triangular = {sumUpperTriangular(list, level)}")

    print()
    print("f.")
    print(f"Sum of prime number in line k = {sumPrime(list, level)}")
    
    print()
    print("g.")
    for row in delLineK(list):
        print(row)

    print()
    print("h.")
    for row in delColumnK(list):
        print(row)
    
    print()
    print("i.")
    for row in insertLineK(list, level):
        print(row)

    print()
    print("j.")
    for row in swapRow(list, level):
        print(row)

    print()
    print("k.")
    for row in deleteMax(list, level):
        print(row) 

    print()
    print("l.")
    for row in deletePrimeCol(list, level):
        print(row)
    print()
    print(findRowPrime(list, level))
       
main()