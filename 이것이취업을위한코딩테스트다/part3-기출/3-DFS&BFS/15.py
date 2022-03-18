# 특정 거리의 도시 찾기
# 인접 리스트를 활용하여, 도시간의 거리를 계산하면 되는데,
# BFS 를 활용하여 출발도시에서 가까운 도시부터 차례로 거리를 계산하면 된다.
# 해당 문제가 BFS/DFS 문제로 분류되어있지만 사실 다익스트라 알고리즘으로 풀어도 된다.

import heapq
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

                if cost > K:
                    return 0

def BFS(start, distance):
    q = deque([start])
    distance[start] = 0

    while q:
        now = q.popleft()

        for i in graph[now]:
            if distance[i] == INF:
                distance[i] = distance[now] + 1
                q.append(i)


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

# dijkstra(X, distance)
BFS(X, distance)

no_city = True
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        no_city = False
if no_city:
    print(-1)
