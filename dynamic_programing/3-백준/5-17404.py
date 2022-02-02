import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, start_cost, distance):
    q = []
    heapq.heappush(q, (start_cost, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now[0]][now[1]] < dist:
            continue

        for i in graph[now[0]][now[1]]:
            cost = dist + i[1]
            if distance[i[0][0]][i[0][1]] > cost:
                distance[i[0][0]][i[0][1]] = cost
                heapq.heappush(q, (cost, i[0]))



N = int(input())
graph = [[[] for _ in range(N)] for _ in range(3)]

start_R, start_G, start_B = map(int, input().split())
for i in range(0, N - 1):
    R, G, B = map(int, input().split())
    graph[0][i].append(((1, i + 1), G))
    graph[0][i].append(((2, i + 1), B))
    graph[1][i].append(((2, i + 1), B))
    graph[1][i].append(((0, i + 1), R))
    graph[2][i].append(((0, i + 1), R))
    graph[2][i].append(((1, i + 1), G))

distance_R = [[INF] * N for _ in range(3)]
distance_G = [[INF] * N for _ in range(3)]
distance_B = [[INF] * N for _ in range(3)]

dijkstra((0, 0), start_R, distance_R)
dijkstra((1, 0), start_G, distance_G)
dijkstra((2, 0), start_B, distance_B)

# print(graph)
# print(distance_R)
# print(distance_G)
# print(distance_B)

print(min(distance_R[1][N - 1], distance_R[2][N - 1],
          distance_G[0][N - 1], distance_G[2][N - 1],
          distance_B[0][N - 1], distance_B[1][N - 1]))

# https://www.acmicpc.net/problem/1149 와 연결되는 문제
# 동적계획법 3 https://www.acmicpc.net/problem/17404
