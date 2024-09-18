











def nana(num, row, column):
    if not (0 <= row < 3 and 0 <= column < 3):
        print ("CANNOT ADD")
    if num[row][column] != 0:
        print ("CANNOT ADD")
    num_people = sum (i == 1 )
    for row in num:
        for i in row:
            if num_people <= 2:
                print ("CANNOT ADD")
    return "CANNOT ADD"
num1 = [[0, 0, 1], [0, 0, 0], [0, 0, 1]]
row1, col1 = 0,0
print(nana(num1, row1, col1))

