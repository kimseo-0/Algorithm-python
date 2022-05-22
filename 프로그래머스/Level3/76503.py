# 모두 0으로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/76503
import sys
sys.setrecursionlimit(10**6)

def DFS_unsoloved(graph, a, cur, parent):
    count = 0
    if len(graph[cur]) == 0:
        count = abs(a[cur])
        a[parent] += a[cur]
        a[cur] = 0
        return count

    for node in graph[cur]:
        graph[node].remove(cur)
        count += DFS_unsoloved(graph, a, node, cur)

    count += abs(a[cur])

    return count

def DFS(graph, a, cur, parent):
    count = 0

    for node in graph[cur]:
        graph[node].remove(cur)
        count += DFS(graph, a, node, cur)

    count += abs(a[cur])
    a[parent] += a[cur]
    a[cur] = 0
    return count

def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = [[] for i in range(len(a))]
    for [i, j] in edges:
        graph[i].append(j)
        graph[j].append(i)

    answer = DFS(graph, a, 0, 0)

    return answer


# solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])
solution([-2, 8, -5, -5, -3, 0, 5, 2], [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]])


# 위 문제를 처음에 읽고 생각했을때,
# 부모 노드를 구해서 DFS 로 탐색하면서 값을 더하면 되겠다고 생각했다.
# 부모 노드를 어떻게 구해야하는가에서 많은 시간을 들였다.
# 결론적으로 "트리 구조는 어떤 노드도 모두 부모 노드가 될 수 있다"
# 자료 구조에 대한 이해가 아직 부족한 것 같다. > 기본 자료 구조들에 대한 복습 필요
