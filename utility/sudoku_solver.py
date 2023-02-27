number_board =  [[7, 8, 0, 4, 0, 0, 1, 2, 0],
[6, 0, 0, 0, 7, 5, 0, 0, 9],
[0, 0, 0, 6, 0, 1, 0, 7, 8],
[0, 0, 7, 0, 4, 0, 2, 6, 0],
[0, 0, 1, 0, 5, 0, 9, 3, 0],
[9, 0, 4, 0, 6, 0, 0, 0, 5],
[0, 7, 0, 3, 0, 0, 0, 1, 2],
[1, 2, 0, 0, 0, 7, 4, 0, 0],
[0, 4, 9, 2, 0, 6, 0, 0, 7]]

def solve_board(board):
    index = is_empty(board)
    if is_empty(board) == False:
        return True
    else:
        row,col = index
    for i in range(1,len(board)+1):
        if isRepeat(board,i,(row,col)):
            board[row][col]= i
            if solve_board(board):
                return True
            board[row][col] = 0


        



def pretty_print(board):
    for x in range(len(board)):
        if x % 3 == 0:
            print("****************************")
        for y in range(len(board[0])):
            if y % 3 == 0:
                print(" | ", end="")
            if y == 8:
                print(board[x][y], end="\n")
            else:
                print(str(board[x][y]) + " ", end="")
    print("****************************")


def isRepeat(board, num, index):

    for i in range(len(board)):
        if num == board[index[0]][i] and i != index[1]:
            return False
    
    for i in range(len(board)):
        if num == board[i][index[1]] and i != index[1] :
            return False

    row = index[1] // 3
    col = index[0] // 3
    for x in range(col*3, col*3 + 3):
        for y in range(row*3, row*3 + 3):
            if num == board[x][y] and index != (x,y):
                return False
    return True

def is_empty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return(x,y)
    return False



print(pretty_print(number_board))
print(solve_board(number_board))
print(pretty_print(number_board))
