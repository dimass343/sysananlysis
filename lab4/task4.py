import math
from io import StringIO
import csv
def get_relation_matrix(connections: list, nodes_number: int) -> list:
    matrix = [[0] * 5 for _ in range(nodes_number)]

    for connection in connections:
        node = int(connection[0]) - 1
        next_node = int(connection[1]) - 1

        matrix[node][0] += 1
        matrix[next_node][1] += 1
        for next_connection in connections:
            if next_connection != connections:
                if next_node == int(next_connection[0]) - 1:
                    matrix[node][2] += 1
                    matrix[int(next_connection[1]) - 1][3] += 1
                elif node == int(next_connection[0]) - 1:
                    matrix[next_node][4] += 1
    for row in matrix:
        if row[4] > 0:
            row[4] -= 1

    return matrix

def task(csv_string):
    connections = csv_string.strip().split('\n')
    connections = [x.split(',') for x in connections]

    nodes_number = int(max(map(max, connections)))
    relation_matrix = get_relation_matrix(connections, nodes_number)

    entropy = 0
    for row in range(nodes_number):
        for col in range(5):
            if relation_matrix[row][col] != 0:
                entropy -= (relation_matrix[row][col] / (nodes_number - 1)) * math.log(relation_matrix[row][col] /
                                                                                       (nodes_number - 1), 2)
    return round(entropy, 2)


