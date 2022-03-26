INF = 10e9

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for i in range(N + 1)]

# 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

# 간선 정보 입력
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print('∞', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
