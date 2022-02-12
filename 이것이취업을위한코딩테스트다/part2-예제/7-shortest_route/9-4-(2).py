import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

X, K = map(int, input().split())

distance1 = [INF] * (N + 1)
distance2 = [INF] * (N + 1)

dijkstra(1, distance1)
dijkstra(K, distance2)

if distance1[K] == INF or distance2[X] == INF:
    print(-1)
else:
    print(distance1[K] + distance2[X])
