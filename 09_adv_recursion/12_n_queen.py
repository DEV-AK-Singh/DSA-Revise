# .00 .01 .02 .03
# .10 .11 .12 .13
# .20 .21 .22 .23
# .30 .31 .32 .33 

def is_safe(pos_r, pos_c, board):  
    i = pos_r
    j = pos_c

    flag = True 

    if j == 0:
        return flag
    
    # print("upper-left")
    while i >= 0 and j >= 0:
        # print(i,j)
        if board[i][j] ==  "Q":
            return False
        i -= 1
        j -= 1 

    # print("left")
    i = pos_r
    j = pos_c
    while j >= 0:
        # print(i,j)
        if board[i][j] ==  "Q":
            return False
        j -= 1 

    # print("down-left")
    i = pos_r
    j = pos_c
    while i <= len(board[0])-1 and j >= 0:
        # print(i,j)
        if board[i][j] ==  "Q":
            return False
        i += 1
        j -= 1 

    return flag

res = []

board = [["."] * 4 for _ in range(4)]

def backtrack(index, board):
    if index == len(board): 
        res.append(["".join(row) for row in board])
        return 

    for row in range(0, len(board)):
        if is_safe(row, index, board):
            board[row][index] =  "Q"
            backtrack(index+1, board)
            board[row][index] =  "."
     
backtrack(0,board)

print(res)

