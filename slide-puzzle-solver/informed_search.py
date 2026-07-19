# informed_search.py

import heapq
from puzzle import move, is_goal, get_heuristic


def informed_search(initial_state):
    """
    Informed Search implementation for the 15-puzzle using a heuristic.

    Args:
        initial_state (tuple): The starting state of the puzzle.

    Returns:
        tuple: (path, nodes_expanded)
            - path (list): The sequence of moves to solve the puzzle.
            - nodes_expanded (int): The number of nodes expanded during the search.
    """
    heap = [(get_heuristic(initial_state), initial_state, [])]  # Heap stores (heuristic, state, path)
    visited = set()  # Set to keep track of visited states
    nodes_expanded = 0  # Counter for nodes expanded

    while heap:
        _, current_state, path = heapq.heappop(heap)
        nodes_expanded += 1

        # Check if the current state is the goal state
        if is_goal(current_state):
            return path, nodes_expanded

        visited.add(current_state)

        # Generate all possible moves from the current state
        for direction in ['U', 'D', 'L', 'R']:
            new_state = move(current_state, direction)
            if new_state and new_state not in visited:
                heapq.heappush(heap, (get_heuristic(new_state), new_state, path + [direction]))

    return None, nodes_expanded