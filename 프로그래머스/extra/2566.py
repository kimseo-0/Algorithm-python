from itertools import permutations


def check(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            print(i)
            return False
    return True

def solution(numbers):
    answer = []
    li = list(numbers)

    for n in range(1, len(li) + 1):
        combination_li = list(map(lambda x: ''.join(s for s in x), list(permutations(li, n))))
        # print(combination_li)

        for num in combination_li:
            if check(int(num)):
                answer.append(int(num))
    # print(answer)
    return len(set(answer))


solution("17")
