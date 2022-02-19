# 순서대로
G = int(input())
P = int(input())
plains = [[]]
gate = [[] for _ in range(G + 1)]
for i in range(P):
    plain = [i for i in range(1, int(input()) + 1)]
    plains.append(plain)
    for j in plain:
        gate[j].append(i)

plains.sort(key=lambda x: len(x))

print(plains)

# for i in range(1, P + 1):

# graph = [[0] * (G + 1) for _ in range(P + 1)]
# for i in range(1, P + 1):
#     for j in range(1, int(input()) + 1):
#         graph[i][j] = 1