# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq
INF = 10e9

def dijkstra(graph, distance, start):
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


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for [a, b, c] in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dijkstra(graph, distance, 1)

    answer = len(list(filter(lambda x: x <= K, distance[1:])))
    print(distance)
    print(answer)
    return answer


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
