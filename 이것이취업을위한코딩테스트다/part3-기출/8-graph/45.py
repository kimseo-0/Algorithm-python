import sys
input = sys.stdin.readline
from collections import deque

def topology_sort(graph, in_degree):
    result = []
    q = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    return result


all_result = []
T = int(input())
for t in range(T):
    N = int(input())
    in_degree = [0] * (N + 1)
    graph = [[] for i in range(N + 1)]

    rank = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            graph[rank[i]].append(rank[j])
            in_degree[rank[j]] += 1

    change_num = int(input())
    for i in range(change_num):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            in_degree[a] += 1
            in_degree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            in_degree[a] -= 1
            in_degree[b] += 1

    # print(graph)
    # print(in_degree)

    result = topology_sort(graph, in_degree)
    all_result.append([N, result])

    # print(result)

for result in all_result:
    [N, result] = result
    if len(result) != N:
        print("IMPOSSIBLE")
    else:
        for i in range(N):
            print(result[i], end=" ")
        print()

