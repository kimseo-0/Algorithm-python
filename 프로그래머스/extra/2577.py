def solution(number, k):
    answer = ''
    li = list(map(int, list(number)))

    start = 0
    end = k + start + 1
    for i in range(k):
        max_num = max(li[start:end])
        max_index = li[start:end].index(max_num)
        answer += str(max_num)
        k = k - max_index

        start += max_index + 1
        end = k + start + 1
        # print(start)
        if k == 0:
            break

    answer += "".join(map(str, li[start:]))
    # print(li[start:])
    print(answer)

    return answer


solution("1924", 2)
solution("123234", 3)
