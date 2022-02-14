import sys
input = sys.stdin.readline

def DFS(graph, v, visited):
    visited[v] = 1

    for node in graph[v]:
        if visited[node] == 0:
            visited[node] = 1
            DFS(graph, node, visited)


N = int(input())
M = int(input())
computer_link_list = [[] for _ in range(N + 1)]
for i in range(M):
    row, col = map(int, input().split())
    computer_link_list[row].append(col)
    computer_link_list[col].append(row)

virus_list = [0] * (N + 1)

DFS(computer_link_list, 1, virus_list)

print(virus_list.count(1) - 1)
