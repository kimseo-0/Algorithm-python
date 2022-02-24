# 순서대로
G = int(input())
P = int(input())
gate = [0] * (G + 1)
count = 0
for p in range(1, P + 1):
    max_gate = int(input())     # 도킹할 수 있는 가장 큰 탑승구 번호
    for g in range(max_gate, 0, -1):
        if gate[g] == 0:
            gate[g] = 1
            count += 1
            break

print(count)
