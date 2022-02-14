import sys
input = sys.stdin.readline

def DFS(graph, x, y):
    global house_num
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0
    house_num += 1
    DFS(graph, x + 1, y)
    DFS(graph, x - 1, y)
    DFS(graph, x, y + 1)
    DFS(graph, x, y - 1)
    return True


N = int(input())
house_map = []
for i in range(N):
    house_map.append(list(map(int, list(input().strip()))))

count_house = []
house_num = 0
count_dong = 0
for i in range(N):
    for j in range(N):
        house_num = 0
        result = DFS(house_map, i, j)
        if result:
            count_house.append(house_num)
            count_dong += 1

print(count_dong)
count_house.sort()
for count in count_house:
    print(count)
