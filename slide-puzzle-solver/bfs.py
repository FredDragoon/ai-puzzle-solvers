# bfs.py

from collections import deque
from puzzle import move, is_goal


def bfs(initial_state):
    """
    Breadth-First Search implementation for the 15-puzzle.

    Args:
        initial_state (tuple): The starting state of the puzzle.

    Returns:
        tuple: (path, nodes_expanded)
            - path (list): The sequence of moves to solve the puzzle.
            - nodes_expanded (int): The number of nodes expanded during the search.
    """
    queue = deque([(initial_state, [])])  # Queue stores (state, path)
    visited = set()  # Set to keep track of visited states
    nodes_expanded = 0  # Counter for nodes expanded

    while queue:
        current_state, path = queue.popleft()
        nodes_expanded += 1

        # Check if the current state is the goal state
        if is_goal(current_state):
            return path, nodes_expanded

        visited.add(current_state)

        # Generate all possible moves from the current state
        for direction in ['U', 'D', 'L', 'R']:
            new_state = move(current_state, direction)
            if new_state and new_state not in visited:
                queue.append((new_state, path + [direction]))

    return None, nodes_expanded