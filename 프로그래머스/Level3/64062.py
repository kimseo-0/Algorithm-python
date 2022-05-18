# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

def check_gap(available, index):
    [prev_index, next_index] = available[index]
    if prev_index != -1:
        available[prev_index][1] = next_index
    available[next_index][0] = prev_index

    # print(available[:8])
    return next_index - prev_index

def solution(stones, k):
    available = [[i - 1, i + 1] for i in range(200001)]

    for i in range(len(stones)):
        stones[i] = [stones[i], i]

    stones.sort()

    sum_num = 0
    for i in range(len(stones)):
        [num, index] = stones[i]

        if i == len(available) - 1:
            sum_num = num
            break

        [next_num, _] = stones[i + 1]

        [prev_index, next_index] = available[index]
        if prev_index != -1:
            available[prev_index][1] = next_index
        available[next_index][0] = prev_index
        max_gap = next_index - prev_index

        if num == next_num:
            continue

        sum_num = num

        if max_gap > k:
            break

    print(sum_num)
    return sum_num


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
