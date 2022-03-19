# 국영수
# python sort key 사용법
N = int(input())

li = []
for i in range(N):
    name, kr, en, math = input().split()
    li.append([int(kr), int(en), int(math), name])

li.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for i in range(N):
    print(li[i][3])
