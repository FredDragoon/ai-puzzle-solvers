from solvers.simple_backtracking import SimpleBacktrackingSolver
from solvers.smart_backtracking import SmartBacktrackingSolver
from puzzles.easy import easy
from puzzles.medium import medium
from puzzles.hard import hard
from puzzles.evil import evil
from utils.print_sudoku import print_sudoku
import time

# Solve Sudoku with a given solver
def solve_sudoku(board, solver, difficulty):
    print(f"\nSolving {difficulty} puzzle with {solver.__class__.__name__}:")
    # using time.perf_counter() for higher precision
    start_time = time.perf_counter()
    if solver.solve(board):
        #print('')
        print_sudoku(board)
    else:
        print("No solution exists.")
    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print(f"Number of trials: {solver.trials}")

# Main function
if __name__ == "__main__":
    puzzles = [("Easy", easy), ("Medium", medium), ("Hard", hard), ("Evil", evil)]
    for difficulty, puzzle in puzzles:
        # Solve with simple backtracking
        solver = SimpleBacktrackingSolver()
        solve_sudoku([row[:] for row in puzzle], solver, difficulty)
        # Solve with smart backtracking
        solver = SmartBacktrackingSolver()
        solve_sudoku([row[:] for row in puzzle], solver, difficulty)