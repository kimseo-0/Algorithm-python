import heapq
import sys
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


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dijkstra(X, distance)

no_city = True
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        no_city = False
if no_city:
    print(-1)
