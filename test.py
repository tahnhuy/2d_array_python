from random import randint

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
    

    for value in position:
        print (f"{value} ")
    print()

    for value in sumRow: 
        print (f"{value} ")
    print()

    for i in range(level - 1):
        for j in range(level - i - 1):
            if sumRow[j] < sumRow[j + 1]:
                temp1 = sumRow[j]
                sumRow[j] = sumRow[j + 1]
                sumRow[j + 1] = temp1

                temp = position[j]
                position[j] = position[j + 1]
                position[j + 1] = temp
    
    for value in position:
        print (f"{value} ")
    print()
    
    for i in range(level):
        row = []
        for j in range(level):
            value = list[position[i]][j]
            row.append(value)
        result.append(row)
    
    for row in result:
        print(row)


list = []
level = 5
for i in range(level):
    row = []
    for j in range(level):
        value = randint(10, 50)
        row.append(value)
    list.append(row)

for row in list:
    print(row)

swapRow(list, level)