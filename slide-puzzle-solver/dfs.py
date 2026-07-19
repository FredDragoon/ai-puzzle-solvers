# dfs.py

import random
from puzzle import move, is_goal

# Node limit for DFS to prevent infinite loops
NODE_LIMIT = 10000


def dfs(initial_state, node_limit=NODE_LIMIT):
    """
    Depth-First Search implementation for the 15-puzzle with a node limit.

    Args:
        initial_state (tuple): The starting state of the puzzle.
        node_limit (int): The maximum number of nodes to expand.

    Returns:
        tuple: (path, nodes_expanded)
            - path (list): The sequence of moves to solve the puzzle.
            - nodes_expanded (int): The number of nodes expanded during the search.
    """
    stack = [(initial_state, [])]  # Stack stores (state, path)
    visited = set()  # Set to keep track of visited states
    nodes_expanded = 0  # Counter for nodes expanded

    while stack:
        current_state, path = stack.pop()
        nodes_expanded += 1

        if is_goal(current_state):
            return path, nodes_expanded

        if nodes_expanded >= node_limit:
            return path, nodes_expanded  # Return partial path if node limit is reached

        visited.add(current_state)

        # Shuffle directions to explore differently
        directions = ['U', 'D', 'L', 'R']
        random.shuffle(directions)

        for direction in directions:
            new_state = move(current_state, direction)
            if new_state and new_state not in visited:
                stack.append((new_state, path + [direction]))

    return path, nodes_expanded  # Return partial path if stack is empty