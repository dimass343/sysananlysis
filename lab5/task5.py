import numpy as np
import json

def get_ranking_len(ranking: list) -> int:
    return sum(1 if isinstance(x, str) else len(x) for x in ranking)

def get_relation_matrix(ranking: list) -> np.ndarray:
    ranks_amount = get_ranking_len(ranking)
    matrix = np.zeros((ranks_amount, ranks_amount), dtype=int)
    for index, group in enumerate(ranking):
        row = np.zeros(ranks_amount, dtype=int)
        for remaining_group in ranking[index:]:
            if isinstance(remaining_group, str):
                row[int(remaining_group) - 1] = 1
            else:
                row[np.array(remaining_group, dtype=int) - 1] = 1
        if isinstance(group, str):
            matrix[int(group) - 1] = row
        else:
            matrix[np.array(group, dtype=int) - 1] = row
    return matrix

def task(l: str, r: str) -> str:
    l = json.loads(l)
    r = json.loads(r)
    matrix_l = get_relation_matrix(l)
    matrix_r = get_relation_matrix(r)

    y = matrix_l * matrix_r
    y_transposed = matrix_l.T * matrix_r.T
    core = y | y_transposed
    conflicts = np.where(core == 0)
    conflict_pairs = [[str(x+1), str(y+1)] for x, y in zip(*conflicts) if x < y]
    return json.dumps(conflict_pairs)