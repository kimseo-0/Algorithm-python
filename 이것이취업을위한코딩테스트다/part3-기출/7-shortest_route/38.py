# 08:20 ~ 08:43
# 2 <= N <= 500
# K번 학생의 앞에 몇명? 뒤에 몇명? 확인 가능하면 > 정확한 성적 순위를 알 수 있다.
# a -> K 경로가 가능하면 a 성적 < K 성적, a는 K 보다 순위가 낮다.
# a <- K 경로가 가능하면 a 성적 > K 성적, a는 K 보다 순위가 높다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]   # 0으로 초기화
for i in range(M):
    a, b = map(int, input().split())    # 성적이 a 성적 < b 성적
    graph[a][b] = 1                     # a와 b 사이의 성적 우열을 가릴 수 있음 : 1

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 1             # a 와 b 가 동일한 번호일 때 : 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][b] == 0:        # 아직 a와 b 사이의 성적 우열을 가릴 수 없을 때(0)
                if graph[a][k] == 1 and graph[k][b] == 1:   # K번째 학생을 가운데 낄 경우 우열을 가릴 수 있다면 : 1
                    graph[a][b] = 1

# for g in graph:
#     print(g)

count = 0  # 순위를 정확히 알 수 있는 학생 수
for k in range(1, N + 1):
    is_count = True     # 순위를 정확하게 알 수 있는지 확인
    for i in range(1, N + 1):
        if graph[k][i] == 0 and graph[i][k] == 0:   # K번째 학생보다 i번째 학생의 순위가 높은지 낮은지 알 수 없을 때
            is_count = False
            break
    if is_count:
        count += 1

print(count)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# > 1
