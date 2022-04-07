# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189
import heapq
INF = 10e9

def solution(n, edge):
    answer = 0
    distance = [INF] * (n + 1)
    distance[1] = 0
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        [a, b] = e
        graph[a].append(b)
        graph[b].append(a)

    # 다익스트라 코드
    q = []
    heapq.heappush(q, 1)

    while q:
        now = heapq.heappop(q)

        for node in graph[now]:
            if distance[node] > distance[now] + 1:
                distance[node] = distance[now] + 1
                heapq.heappush(q, node)

    # 긴 노드 갯수 세기
    distance.count(max(distance[1:]))

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])