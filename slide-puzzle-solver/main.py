# main.py

import time
import psutil
import os
from puzzle import INITIAL_STATE
from bfs import bfs
from dfs import dfs
from informed_search import informed_search


def get_memory_usage():
    """
    Get the current process memory usage in KB.

    Returns: Memory usage in KB.
    """
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024  # Converts to KB


def main():
    """
    Main function to run all search algorithms and print results.
    """
    algorithms = {
        "BFS": bfs,
        "DFS": dfs,
        "Informed Search": informed_search
    }

    for name, algorithm in algorithms.items():
        start_time = time.time()
        start_memory = get_memory_usage()
        path, nodes_expanded = algorithm(INITIAL_STATE)
        end_memory = get_memory_usage()
        end_time = time.time()

        print(f"{name}")
        if path:
            print(f"Moves: {''.join(path)}")
        print(f"Number of nodes expanded: {nodes_expanded}")
        print(f"Time taken: {(end_time - start_time) * 1000:.2f}ms")
        print(f"Memory used: {end_memory - start_memory:.2f} KB")
        if path:
            print("Solution exists")
        else:
            print("Solution doesn't exist (or not found within node limit)")
        print()


if __name__ == "__main__":
    main()