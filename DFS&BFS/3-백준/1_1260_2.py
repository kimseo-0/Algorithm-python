import sys
from collections import deque

input = sys.stdin.readline

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for node in graph[v]:
        if not visited[node]:
            DFS(graph, node, visited)

def BFS(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


N, M, V = map(int, input().split())
linked_list = [[] for _ in range(N + 1)]
for i in range(M):
    row, col = map(int, input().split())
    linked_list[row].append(col)
    linked_list[col].append(row)

# 여러개의 노드가 있을 경우 작은 것을 우선순위 위에 둔다는 조건
for li in linked_list:
    li.sort()

visited_list = [False] * (N + 1)
DFS(linked_list, V, visited_list)
print()
visited_list = [False] * (N + 1)
BFS(linked_list, V, visited_list)

'''
연결 리스트를 활용한 풀이
'''