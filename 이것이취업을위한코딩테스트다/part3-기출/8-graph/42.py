# 순서대로
# G = int(input())
# P = int(input())
# gate = [0] * (G + 1)
# count = 0
# for p in range(1, P + 1):
#     max_gate = int(input())     # 도킹할 수 있는 가장 큰 탑승구 번호
#     for g in range(max_gate, 0, -1):
#         if gate[g] == 0:
#             gate[g] = 1
#             count += 1
#             break
#
# print(count)

# 서로소 집합을 활용한 풀이
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


G = int(input())
P = int(input())
gate = [0] * (G + 1)

for i in range(1, G + 1):
    gate[i] = i

count = 0
for p in range(1, P + 1):
    max_gate_num = int(input())
    parent_num = find_parent(gate, max_gate_num)

    if parent_num == 0:
        break

    count += 1
    union_parent(gate, parent_num, parent_num - 1)

print(count)
