def solution1(numbers):
    answer = ''

    num_list = [[] for _ in range(10)]
    num_count = [0] * 10

    for num in numbers:
        if num < 10:
            num_list[num].append(num)
            num_count[num] += 1
        elif num < 100:
            num_list[num//10].append(num)
            num_count[num//10] += 1
        elif num < 1000:
            num_list[num//100].append(num)
            num_count[num//100] += 1
        else:
            num_list[1].append(1000)
            num_count[1] += 1

    print(num_list)
    print(num_count)

    return answer

def solution2(numbers):
    answer = ''

    num_list = [[] for _ in range(10)]
    num_count = [0] * 10

    for num in numbers:
        if num < 10:
            num_list[num].append(list(str(num)))
            num_count[num] += 1
        elif num < 100:
            num_list[num // 10].append(list(str(num)))
            num_count[num // 10] += 1
        elif num < 1000:
            num_list[num // 100].append(list(str(num)))
            num_count[num // 100] += 1
        else:
            num_list[1].append(list(str(1000)))
            num_count[1] += 1

    print(num_list)
    print(num_count)

    for i in range(9, -1, -1):
        num_list[i].sort()

    print(num_list)
    return answer


def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))


solution([3, 30, 34, 9, 5, 96, 954])





