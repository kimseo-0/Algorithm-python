# H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        answer = i + 1
        if i + 1 == citations[i]:
            answer = i + 1
            break
        elif i + 1 > citations[i]:
            answer = i
            break
    print(answer)
    return answer


# solution([2, 0, 6, 1, 5, 4])
# solution([2, 0, 6, 1, 5])
# solution([3, 0, 6, 1, 5])
# solution([1, 1, 1, 2, 2])
# solution([4, 4, 4])
# solution([1, 1, 1])
solution([0, 0, 0])
