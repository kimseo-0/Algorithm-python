# 소수 찾기
from itertools import permutations


def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    num_list = list(numbers)

    for i in range(1, len(numbers) + 1):
        permutation_list = permutations(num_list, i)
        for permutation in permutation_list:
            num = int("".join(permutation))
            if num == 0 or num == 1:
                continue
            if num not in answer:
                if check(num):
                    answer.append(num)

    print(answer)
    return len(answer)


solution("17")
solution("011")


# "에라토스테네스 체" - 단일 숫자 소수 여부 확인
# https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
# 1. 배열을 생성하여 초기화한다.
# 2. 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.(지울 때 자기자신은 지우지 않고, 이미 지워진 수는 건너뛴다.)
# 3. 2부터 시작하여 남아있는 수를 모두 출력한다.

def solution1(numbers):
    num_list = set()

    for i in range(1, len(numbers) + 1):
        num_list |= set(map(int, map("".join, permutations(list(numbers), i))))

    num_list -= set(range(0, 2))

    for i in range(2, int(max(num_list) ** 0.5) + 1):
        num_list -= set(range(i * 2, max(num_list) + 1, i))

    print(num_list)
    return len(num_list)

def Eratosthenes(num):
    num_list = [i for i in range(num + 1)]
    for i in range(2, int(max(num_list) ** 0.5) + 1):
        for j in range(i * 2, max(num_list) + 1, i):
            num_list[j] = 0

    num_list = list(filter(lambda x: x > 0, num_list))
    print(num_list)


solution1("17")
Eratosthenes(20)
