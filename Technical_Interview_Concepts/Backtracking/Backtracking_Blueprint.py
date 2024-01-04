"""
Backtracking Crash Course and Blueprint to solve the problem.

"""


def is_valid_state(state):
    return True


def get_candidate(state):
    return []


def search(state, solution):
    if is_valid_state(state):
        solution.append(state.copy)
