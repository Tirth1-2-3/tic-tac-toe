import random
def check_if_over (list_1):
    row_1 = (list_1[0][0] == list_1[0][1] == list_1[0][2] != '_')
    row_2 = (list_1[1][0] == list_1[1][1] == list_1[1][2] != '_')
    row_3 = (list_1[2][0] == list_1[2][1] == list_1[2][2] != '_')
    col_1 = (list_1[0][0] == list_1[1][0] == list_1[2][0] != '_')
    col_2 = (list_1[0][1] == list_1[1][1] == list_1[2][1] != '_')
    col_3 = (list_1[0][2] == list_1[1][2] == list_1[2][2] != '_')
    cross_1 = (list_1[0][0] == list_1[1][1] == list_1[2][2] != '_')
    cross_2 = (list_1[0][2] == list_1[1][1] == list_1[2][0] != '_')
    return (row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or cross_1 or cross_2)
def print_matrix (list_2):
    print(f'{list_2[0][0]} {list_2[0][1]} {list_2[0][2]}')
    print(f'{list_2[1][0]} {list_2[1][1]} {list_2[1][2]}')
    print(f'{list_2[2][0]} {list_2[2][1]} {list_2[2][2]}')
matrix = [['_','_','_'],['_','_','_'],['_','_','_']]
list_3 = [['','',''],['','',''],['','','']]
while(check_if_over(matrix)==False):
    temp_1 = int(input('Enter row: '))
    temp_2 = int(input('Enter col: '))
    val = input('Enter x/o: ')
    list_3[temp_1][temp_2] = val 
    matrix[temp_1][temp_2] = val
    if (check_if_over(matrix) == True):
        print_matrix(matrix)
        print('You Won!')
        break
    while(True):
        rand_row = random.randint(0,2)
        rand_col = random.randint(0,2)
        if (list_3[rand_row][rand_col]==''):
            break
    rand_sign = random.randint(0,1)
    if (rand_sign == 0):
        rand_sign = 'x'
    else:
        rand_sign = 'o'
    matrix[rand_row][rand_col] = rand_sign
    print_matrix(matrix)
    if (check_if_over(matrix) == True):
        print('You lost!')
        break





