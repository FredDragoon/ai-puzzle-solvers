from solvers.base_solver import SudokuSolver

class SmartBacktrackingSolver(SudokuSolver):
    def find_empty_cell(self, board):
        min_values = 10
        best_cell = None
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    possible_values = self.get_possible_values(board, row, col)
                    if len(possible_values) < min_values:
                        min_values = len(possible_values)
                        best_cell = (row, col)
        return best_cell

    def get_possible_values(self, board, row, col):
        values = set(range(1, 10))
        for i in range(9):
            values.discard(board[row][i])
            values.discard(board[i][col])
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                values.discard(board[start_row + i][start_col + j])
        return list(values)

    def solve(self, board):
        cell = self.find_empty_cell(board)
        if not cell:
            return True
        row, col = cell
        for num in self.get_possible_values(board, row, col):
            self.trials += 1
            board[row][col] = num
            if self.solve(board):
                return True
            board[row][col] = 0
        return False