# https://www.acmicpc.net/problem/11404
# 플로이드 워셜 알고리즘 문제임
# 시작 도시와 도착 도시를 연결하는 노선이 여러 개 가능 > 입력시 min 값 처리
# 갈 수 없는 경우 0 > INF 일경우 0 출력
import sys
input = sys.stdin.readline
INF = 10e9


N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] >= INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
