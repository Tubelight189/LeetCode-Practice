def solveSudoku(board):
    rows=[set()for _ in range(9)]
    cols=[set()for _ in range(9)]
    boxes=[set()for _ in range(9)]
    empty = []
    for i in range(9):
        for j in range(9):
            if board[i][j]!=".":
                val=board[i][j]
                rows[i].add(val)
                cols[j].add(val)
                boxes[(i//3)*3+j//3].add(val)
            else:
                empty.append((i, j))
    def sudoku(idx):
        if idx == len(empty): return True
        x, y = empty[idx]
        box_id = (x // 3) * 3 + y // 3
        for num in "123456789":
            if num not in rows[x] and num not in cols[y] and num not in boxes[box_id]:
                board[x][y] = num
                rows[x].add(num)
                cols[y].add(num)
                boxes[box_id].add(num)
                if sudoku(idx + 1): return True
                board[x][y] = "."
                rows[x].remove(num)
                cols[y].remove(num)
                boxes[box_id].remove(num)
        return False
    sudoku(0)
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