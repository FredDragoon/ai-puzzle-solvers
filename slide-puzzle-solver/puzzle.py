# puzzle.py

# Initial state of the 15-puzzle
INITIAL_STATE = ((1,0,2,4),(5,7,3,8),(9,6,11,12),(13,10,14,15))

# Goal state of the 15-puzzle
GOAL_STATE = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0))

# Directions for moving the blank tile (0)
DIRECTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def find_blank(state):
    """
    Find the position of the blank tile (0) in the puzzle.

    Args:
        state (tuple): The current state of the puzzle.

    Returns:
        tuple: (row, column) of the blank tile.
    """
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile == 0:
                return (i, j)
    return None


def move(state, direction):
    """
    Move the blank tile in the specified direction.

    Args:
        state (tuple): The current state of the puzzle.
        direction (str): The direction to move the blank tile ('U', 'D', 'L', 'R').

    Returns:
        tuple: The new state after moving the blank tile, or None if the move is invalid.
    """
    blank_row, blank_col = find_blank(state)
    new_row, new_col = blank_row + DIRECTIONS[direction][0], blank_col + DIRECTIONS[direction][1]

    # Check if the new position is within the puzzle boundaries
    if 0 <= new_row < 4 and 0 <= new_col < 4:
        state = [list(row) for row in state]  # Convert tuple to list for mutability
        # Swap the blank tile with the tile in the new position
        state[blank_row][blank_col], state[new_row][new_col] = state[new_row][new_col], state[blank_row][blank_col]
        return tuple(map(tuple, state))  # Convert back to tuple
    return None


def is_goal(state):
    """
    Check if the current state is the goal state.

    Args:
        state (tuple): The current state of the puzzle.

    Returns:
        bool: True if the state is the goal state, False otherwise.
    """
    return state == GOAL_STATE


def get_heuristic(state):
    """
    Calculate the heuristic value (number of misplaced tiles).

    Args:
        state (tuple): The current state of the puzzle.

    Returns:
        int: The number of tiles that are not in their goal position.
    """
    return sum(1 for i in range(4) for j in range(4) if state[i][j] != GOAL_STATE[i][j])