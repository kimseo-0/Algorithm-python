import sys
input = sys.stdin.readline

# 1차 방법
# N = int(input())
# N = 5
#
# count = 0
# start_time = [0, 0, 0]  # 시 분 초 > 시계처럼 동작하게 코드를 구현함
# while True:
#     sum += 1
#     for time_part in start_time:
#         if '3' in str(time_part):
#             count += 1
#             break
#
#     # 시계 동작 구현
#     start_time[2] += 1
#     if start_time[2] == 60:
#         start_time[2] = 0
#         start_time[1] += 1
#     if start_time[1] == 60:
#         start_time[1] = 0
#         start_time[0] += 1
#     # N+1 시가 되면 종료
#     if start_time[0] == N+1:
#         break
#
# print(count)

# 2차 방법
# 시계를 구현하지 않고 데이터 상으로만 구현할 수 있다
# N = int(input())
N = 5
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if (str(i)+str(j)+str(k)).find("3") != -1:  # "3" in (str(i)+str(j)+str(k))
                count += 1

print(count)
