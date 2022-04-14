# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677


def solution(str1, str2):
    count = {}
    intersection_num = 0
    union_num = 0
    for i in range(1, len(str1)):
        word = str1[i - 1: i + 1].lower()
        if word.isalpha():
            union_num += 1
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    for i in range(1, len(str2)):
        word = str2[i - 1: i + 1].lower()
        if word.isalpha():
            if word in count:
                count[word] -= 1
                intersection_num += 1
                if count[word] == 0:
                    count.pop(word)
            else:
                union_num += 1

    if union_num == 0:
        answer = 1
    else:
        answer = intersection_num / union_num
    answer = int(answer * 65536)
    print(answer)
    return answer


solution('FRANCE!', 'french')
