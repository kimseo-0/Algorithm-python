import sys
from collections import deque

input = sys.stdin.readline

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for index in range(1, N + 1):
        if (graph[v][index] == 1) and not visited[index]:
            DFS(graph, index, visited)

def BFS(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for index in range(1, N + 1):
            if (graph[v][index] == 1) and not visited[index]:
                visited[index] = True
                queue.append(index)


N, M, V = map(int, input().split())
linked_matrix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    row, col = map(int, input().split())
    linked_matrix[row][col] = 1
    linked_matrix[col][row] = 1

visited_list = [False] * (N + 1)
DFS(linked_matrix, V, visited_list)
print()
visited_list = [False] * (N + 1)
BFS(linked_matrix, V, visited_list)

'''
연결 행렬을 활용한 풀이
'''