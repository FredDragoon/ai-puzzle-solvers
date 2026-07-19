from solvers.base_solver import SudokuSolver

class SimpleBacktrackingSolver(SudokuSolver):
    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        self.trials += 1
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True