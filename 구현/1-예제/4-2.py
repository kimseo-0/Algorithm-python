import sys
input = sys.stdin.readline

# N = int(input())
N = 5

count = 0
start_time = [0, 0, 0]  # 시 분 초
while True:
    sum += 1
    for time_part in start_time:
        if '3' in str(time_part):
            count += 1
            break

    start_time[2] += 1
    if start_time[2] == 60:
        start_time[2] = 0
        start_time[1] += 1
    if start_time[1] == 60:
        start_time[1] = 0
        start_time[0] += 1
    if start_time[0] == N+1:
        break

print(count)
