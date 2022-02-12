
# python 파일 입출력
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
import sys
input = sys.stdin.readline

N = int(input())
time_list = []
for i in range(N):
    start, end = map(int, input().split())
    time_list.append([start, end])
time_list.sort()

select_list = [time_list[0]]
for time in time_list[1:]:
    # 해당 조건식에서 start == end 인 경우는 elif 로 넘어가도록 부등호를 잘 확인해야한다
    # 결국 문제에 있는 조건을 잘 읽어라
    if time[1] < select_list[-1][1]:
        select_list[-1] = time
    elif time[0] >= select_list[-1][1]:
        select_list.append(time)

print(len(select_list))

# 위 문제를 해결하지 않을 경우 에러가 발생하는 예제
# time_list = [[8, 9], [3, 7], [4, 5], [9, 10], [8, 8], [5, 6], [0, 1], [10, 10]]
# time_list.12-정렬(sort)()
# print(time_list)

# 다른 풀이 방법
# end time을 기준으로 정렬을 한다
# https://www.acmicpc.net/source/37732323

N = int(input())
time_list = []
for i in range(N):
    time_list.append(list(map(int, input().split())))
time_list.sort(key=lambda x: (x[1], x[0]))

end_time = time_list[0][1]
count = 1
for time in time_list[1:]:
    if end_time <= time[0]:
        end_time = time[1]
        count += 1
print(count)
