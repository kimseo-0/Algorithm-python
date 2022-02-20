# 리스트에서 바로 옆 요소와 비교를 하는 경우

def compression(str_list, n):
    result = 0

    count = 1
    word = str_list[0:n]
    for i in range(1, (len(str_list) // n)):
        if word == str_list[(n * i):(n * i) + n]:
            count += 1
        else:
            if count == 1:
                result += n
            else:
                result += n + len(str(count))
            word = str_list[(n * i):(n * i) + n]
            count = 1

    if count == 1:
        result += n
    else:
        result += n + len(str(count))

    # 나머지
    result = result + (len(str_list) % n)
    return result


def compression2(str_list, n):
    result = []
    count = 1
    word = str_list[0:n]
    for i in range(1, (len(str_list) // n)):
        if word == str_list[(n * i):(n * i) + n]:
            count += 1
        else:
            result.append([word, count])
            word = str_list[(n * i):(n * i) + n]
            count = 1
    result.append([word, count])
    print(result)
    # result = result + (len(str_list) % n)
    return sum(len(word) + (len(str(count)) if count > 1 else 0) for word, count in result) + (len(str_list) % n)


def solution(s):
    str_list = list(s)
    answer = len(str_list)
    for i in range(1, len(str_list)):
        answer = min(compression(str_list, i), answer)
    return answer

# print(solution("a"))
