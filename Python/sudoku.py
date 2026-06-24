def possible(board,x,y,number):
    for i in range(9):
        if board[x][i] == str(number): return False
        if board[i][y] == str(number): return False
    xbox=(x//3)*3
    ybox=(y//3)*3
    for i in range(3):
        for j in range(3):
            if board[xbox+i][ybox+j]==str(number):return False
    return True
def sudoku(board):
    # for row in board:
    #     if "." in row:break
    # else:return True
    for x in range(9):
        for y in range(9):
            if board[x][y]==".":
                for num in range(1,10):
                    if possible(board,x,y,num):
                        board[x][y]=str(num)
                        if sudoku(board):return True
                        board[x][y]="."
                return False
    return True
def solveSudoku(board):
    sudoku(board)
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solveSudoku(board)
for _ in range(len(board)):print(board[_])