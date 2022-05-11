# 베스트 앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0] = (dic[genres[i]][0][0] + plays[i], -1)
            dic[genres[i]].append((plays[i], i))
        else:
            dic[genres[i]] = [(plays[i], -1), (plays[i], i)]

    values = list(dic.values())
    values.sort(key=lambda x: -x[0][0])

    answer = []
    for i in range(len(values)):
        sorted_value = sorted(values[i], key=lambda x: (-x[0], x[1]))
        for j in range(1, len(values[i])):
            if j > 2:
                break
            answer.append(sorted_value[j][1])

    # print(answer)
    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])