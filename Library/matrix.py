def rotation_matrix_90(matrix, n):
    rotation_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.insert(0, matrix[j][i])
        rotation_matrix.append(row)
    return rotation_matrix

def padding_matrix(matrix, n, padding_len):
    for i in range(padding_len):
        matrix[i] = [*([0] * padding_len), *matrix[i], *([0] * padding_len)]
    for i in range(padding_len - 1):
        matrix.insert(0, [0] * (n + (padding_len * 2)))
        matrix.append([0] * (n + (padding_len * 2)))
