# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

def check_gap(available, index):
    [prev_index, next_index] = available[index]
    if prev_index != -1:
        available[prev_index][1] = next_index
    available[next_index][0] = prev_index

    # print(available[:8])
    return next_index - prev_index

def solution_loof(stones, k):
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

        max_gap = check_gap(available, index)
        if num == next_num:
            continue

        sum_num = num

        if max_gap > k:
            break

    print(sum_num)
    return sum_num

def solution_binary(stones, k):
    start = 0
    end = max(stones)
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        count = 0
        max_gap = 0
        for stone in stones:
            if stone - mid < 0:
                count += 1
            else:
                count = 0

            # else 문 내에서 할 경우 마지막 인덱스는 체크하지 않는 경우 발생
            if max_gap < count:
                max_gap = count

        print(mid, max_gap)
        if max_gap >= k:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    print(answer)
    return answer


solution_binary([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1)
