__author__ = 'changhan.ryu'


input_str1, input_str2 = input("input the number").split()
var1 = int(input_str1)
var2 = int(input_str2)
board = []
row_index = 0
col_index = 0
whole_num_index = 0
row = [x for x in range(var1)]
col = [y for y in range(var2)]
whole_num = [z for z in range(var1 * var2)]

# make a dull M*N matrix
def dull_matrix(var1):
    for x in range(var1):
        board.append(["0"] * var1)

def print_board(board):
    for row in board:
        print("".join(row))

# move left in a row
def move_left_row():

    for i in range(len(col)):
        board[r][i] = str(whole_num[i])
        w += 1
    r += 1
    return row_index, col_index, whole_num_index


# move down in a col
def move_down_col():
    for i in range(len(low)):
        board[col_index]


# move downward in a column
for i in range(1, len(col)):
    board[i][len(col)-1] = str(whole_num[index+1:len(col)])