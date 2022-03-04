import heapq
import sys
input = sys.stdin.readline
INF = 10e9

def dijkstra(graph, distance, start):
    q = []
    (cost, x) = start
    heapq.heappush(q, (cost, x))
    distance[x] = [cost, x]

    while q:
        dist, x = heapq.heappop(q)
        if distance[x][0] < dist:
            continue

        for new_cost, nx in graph[x]:
            cost = dist + new_cost
            if distance[nx][0] > cost:
                distance[nx] = [cost, nx]
                heapq.heappush(q, (cost, nx))


N, M = map(int, input().split())

route = [[] for _ in range(N + 1)]
base_distance = [[INF, 0] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    route[a].append((1, b))
    route[b].append((1, a))

dijkstra(route, base_distance, (0, 1))
base_distance.sort(reverse=True)
min_index = N
max_cost = 0
count = 0
for cost, index in base_distance:
    if cost >= INF:
        continue
    if max_cost > cost:
        break
    max_cost = cost
    min_index = index
    count += 1

# print(route)
# print(base_distance)
print(min_index, max_cost, count)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
