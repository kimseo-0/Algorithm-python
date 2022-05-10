# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for [i, j, f] in fares:
        graph[i][j] = f
        graph[j][i] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # for i in graph:
    #     print(i)

    answer = int(1e9)
    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    # print(answer)
    return answer


solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
