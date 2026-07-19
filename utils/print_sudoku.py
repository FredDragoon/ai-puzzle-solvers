def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))