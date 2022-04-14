def rotation(graph, row1, col1, row2, col2):
    row = row1
    col = col1
    result = graph[row + 1][col]
    temp1 = graph[row + 1][col]
    temp2 = graph[row + 1][col]
    for i in range(col2 - col1):
        result = min(graph[row][col + i], result)
        temp2 = graph[row][col + i]
        graph[row][col + i] = temp1
        temp1 = temp2
    col += col2 - col1
    for i in range(row2 - row1):
        result = min(graph[row + i][col], result)
        temp2 = graph[row + i][col]
        graph[row + i][col] = temp1
        temp1 = temp2
    row += row2 - row1
    for i in range(col2 - col1):
        result = min(graph[row][col - i], result)
        temp2 = graph[row][col - i]
        graph[row][col - i] = temp1
        temp1 = temp2
    col -= col2 - col1
    for i in range(row2 - row1):
        result = min(graph[row - i][col], result)
        temp2 = graph[row - i][col]
        graph[row - i][col] = temp1
        temp1 = temp2

    return result

def solution(rows, columns, queries):
    answer = []

    graph = [[columns * (j - 1) + i for i in range(1, columns + 1)] for j in range(1, rows + 1)]
    for i in graph:
        for j in i:
            print(j, end="\t")
        print()
    for querie in queries:
        [row1, col1, row2, col2] = querie
        answer.append(rotation(graph, row1 - 1, col1 - 1, row2 - 1, col2 - 1))
    # for i in graph:
    #     for j in i:
    #         print(j, end="\t")
    #     print()
    print(answer)
    return answer


# solution(6, 6, [[2,2,5,4], [3,3,6,6], [5,1,6,3]])
# solution(100, 97, [[1, 1, 100, 97]])
# solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
# solution(6, 5, [[1, 1, 6, 5]])
# solution(4, 6, [[1, 1, 4, 4]])
solution(4, 2, [[1, 1, 2, 2]])
