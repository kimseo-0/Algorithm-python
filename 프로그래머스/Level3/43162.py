# 깊이/너비 우선 탐색(DFS/BFS) > 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, computers):
    parent_list = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i <= j:
                continue
            if computers[i][j] == 1:
                union_parent(parent_list, i, j)

    for i in range(n):
        find_parent(parent_list, i)

    answer = len(set(parent_list))
    print(parent_list)
    return answer


solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
