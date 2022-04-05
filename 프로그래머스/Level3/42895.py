# https://programmers.co.kr/learn/courses/30/lessons/42895
# N으로 표현

def cal_array(arr1, arr2, answer):
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            result.append(arr1[i] + arr2[j])
            result.append(arr1[i] * arr2[j])
            result.append(arr1[i] - arr2[j])
            result.append(arr2[j] - arr1[i])
            if arr1[i] != 0:
                result.append(arr2[j] // arr1[i])
            if arr2[j] != 0:
                result.append(arr1[i] // arr2[j])

    return list(set(result))

def solution(N, number):
    if N == number:
        return 1

    DP = [[] for i in range(9)]
    for i in range(1, 9):
        DP[i].append(int(str(N) * i))

    for n in range(2, 9):
        for i in range(1, n):
            DP[n].extend(cal_array(DP[i], DP[n - i], number))
        if number in DP[n]:
            # print(DP[n])
            return n

    return -1


print(solution(5, 31168))
# print(solution(2, 11))
