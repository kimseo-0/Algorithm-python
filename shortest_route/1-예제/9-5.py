import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
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


N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


distance = [INF] * (N + 1)
dijkstra(C)

count = 0
max_distance = 0
for i in range(1, N + 1):
    if distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])

print(count - 1, end=' ')
print(max_distance)
print(distance)
