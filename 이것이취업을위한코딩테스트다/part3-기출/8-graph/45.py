# 최종순위
# 확실한 순위를 찾을 수 없는 경우가 없기 때문에 ? 출력은 구현하지 않아도 맞았지만
# 문제를 제대로 읽지 않았다는 점에서 문제가 있다.

# ? 출력 : 확실한 순위를 찾을 수 없는 경우, 진입차수가 0인 경우가 2개 이상이 있는 경우
# IMPOSSIBLE 출력 : 데이터에 일관성이 없는 경우, cycle 이 발생한 경우

import sys
input = sys.stdin.readline
from collections import deque

def topology_sort(graph, in_degree):
    certain = True
    result = []
    q = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        if len(q) > 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    return result, certain


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

    result, certain = topology_sort(graph, in_degree)
    all_result.append([N, result, certain])

    # print(result)

for result in all_result:
    [N, result, certain] = result
    if not certain:
        print("?")
    elif len(result) != N:
        print("IMPOSSIBLE")
    else:
        for i in range(N):
            print(result[i], end=" ")
        print()

