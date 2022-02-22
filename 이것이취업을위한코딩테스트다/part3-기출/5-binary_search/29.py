import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house_list = []
for i in range(N):
    house_list.append(int(input()))
house_list.sort()
max_distance = (house_list[-1] - house_list[0]) // (C - 1)

result_distance = house_list[-1] - house_list[0]

start = 1
end = N - 2
start_house = house_list[start - 1]
for i in range(2, C):
    target = house_list[start - 1] + max_distance
    min_distance = house_list[end + 1] - house_list[start - 1]
    result_mid = 0
    while start <= end:
        mid = (start + end) // 2

        if house_list[mid] == target:
            result_mid = mid
            break
        elif house_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

        if min_distance > abs(target - house_list[mid]):
            min_distance = abs(target - house_list[mid])
            result_mid = mid

    result_distance = min(result_distance, house_list[result_mid] - start_house)
    start = result_mid + 1
    end = N - 2
    start_house = house_list[start]

    if i == C - 1:
        result_distance = min(result_distance, house_list[-1] - house_list[result_mid])

print(result_distance)

