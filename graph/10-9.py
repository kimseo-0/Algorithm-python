from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            # all_class_time[i] = max(all_class_time[i], all_class_time[now] + class_time[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    return result


N = int(input())
class_time = [0] * (N + 1)
all_class_time = [0] * (N + 1)
in_degree = [0] * (N + 1)

graph = [[] for i in range(N + 1)]
re_graph = [[] for i in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    class_time[i] = line[0]
    all_class_time[i] = line[0]
    for j in line[1:]:
        if j == -1:
            break
        graph[j].append(i)
        re_graph[i].append(j)
        in_degree[i] += 1


result = topology_sort()

print(result)
print(re_graph)

for i in result:
    for j in re_graph[i]:
        all_class_time[i] = max(all_class_time[i], all_class_time[j] + class_time[i])

for i in range(1, N + 1):
    print(all_class_time[i])
