# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def DFS(numbers, index, result, target, count):
    if index >= len(numbers):
        if result == target:
            return count + 1
        return count

    count = DFS(numbers, index + 1, result + numbers[index], target, count)
    count = DFS(numbers, index + 1, result - numbers[index], target, count)

    return count


def solution(numbers, target):
    answer = DFS(numbers, 0, 0, target, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
