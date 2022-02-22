import sys
input = sys.stdin.readline

N = int(input())
time_table = []  # [[T, P],[]]
for i in range(N):
    time_table.append(list(map(int, input().split())))

# (i + 1) 상담을 무조건 한다고 가정했을 때, 최대 수익
DP = [0] * N

# 현재 날짜
for i in range(N):
    # 현재 상담 일정을 기간 내에 끝낼 수 없는 경우
    if i + time_table[i][0] > N:
        continue

    # 현재 상담 페이 초기화
    DP[i] = time_table[i][1]

    # 과거 ~ 오늘까지 상담 일정 체크
    for j in range(i):
        if i >= j + time_table[j][0]:
            DP[i] = max(DP[j] + time_table[i][1], DP[i])

print(max(DP))
