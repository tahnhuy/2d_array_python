from random import randint

def inputValue(list, rows, cols):
    for i in range(0, rows):
        row = []
        for i in range(0, cols):
            row.append(randint(0, 50))

        list.append(row)

    return list

def arrangeRow(list, rows, cols):
    for k in range(0, rows):
        for i in range(0, cols - 1):
            for j in range(0, cols - i - 1):
                if list[k][j] > list[k][j + 1]:
                    temp = list[k][j]
                    list[k][j] = list[k][j + 1]
                    list[k][j + 1] = temp

    return list

def arrangeCol(list, rows, cols):
    for k in range(0, cols):
        for i in range(0, rows - 1):
            for j in range(0, rows - i - 1):
                if list[j][k] > list[j + 1][k]:
                    temp = list[j][k]
                    list[j][k] = list[j + 1][k]
                    list[j + 1][k] = temp
    
    return list

list = []

rows = int(input("Enter numbers of rows: "))
cols = int(input("Enter numbers of columns: "))

inputValue(list, rows, cols)
for row in list:
    print(row)

print(' ')

arrangeRow(list, rows, cols)
for row in list:
    print(row)

print(' ')

arrangeCol(list, rows, cols)
for row in list:
    print(row)