import numpy as np
import json


def get_comparison_matrix(input_columnes):
    matrix = np.zeros((len(input_columnes), len(input_columnes)))
    for rows_wid, row in enumerate(matrix):
        for col_ind, col in enumerate(row):
            if input_columnes[rows_wid] < input_columnes[col_ind]:
                matrix[rows_wid, col_ind] = 1
            elif input_columnes[rows_wid] == input_columnes[col_ind]:
                matrix[rows_wid, col_ind] = 0.5
            else:
                matrix[rows_wid, col_ind] = 0
    return matrix


def task(json_input):
    input_list = np.array(json.loads(json_input)).T
    comparison_matrices = []
    for input_col in input_list.T:
        comparison_matrices.append(get_comparison_matrix(input_col))

    general_matricies = np.zeros((len(input_list), len(input_list)))
    for i in range(len(input_list)):
        general_matricies += comparison_matrices[i]
    general_matrix = general_matricies / len(input_list)

    keyzero = np.array([1 / len(input_list)] * len(input_list))
    ykeys = general_matrix.dot(keyzero)
    lambda1 = (np.ones(len(input_list))).dot(ykeys)
    key10e = 1 / lambda1 * ykeys
    while abs(max(key10e - keyzero)) >= 0.001:
        keyzero = key10e
        ykeys = general_matrix.dot(keyzero)
        lambda1 = (np.ones(len(input_list))).dot(ykeys)
        key10e = 1 / lambda1 * ykeys
    key10e = np.around(key10e, 3)
    return json.dumps(key10e.tolist())
