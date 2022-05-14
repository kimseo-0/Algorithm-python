# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

def compare(array, query):
    for i in range(5):
        if query[i] == '-':
            continue
        if array[i] < query[i]:
            return -1
        elif array[i] > query[i]:
            return 1
    return 0

def binary_search_first(array, query):
    start = 0
    end = len(array) - 1
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        if int(array[mid]) >= int(query):
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer

def DFS(dic, query, index, keys):
    count = 0
    if index == 4:
        if len(dic) == 0:
            return 0
        else:
            first = binary_search_first(dic, query[index])
            if first == -1:
                return 0
            return len(dic) - first

    if query[index] == '-':
        for key in keys[index]:
            new_dic = dic[key]
            count += DFS(new_dic, query, index + 1, keys)
    else:
        new_dic = dic[query[index]]
        count += DFS(new_dic, query, index + 1, keys)

    return count

def solution(info_list, query_list):
    answer = []

    keys = [['cpp', 'java', 'python'], ['backend', 'frontend'], ['junior', 'senior'], ['chicken', 'pizza']]
    dic = {}
    for a in keys[0]:
        dic_b = {}
        for b in keys[1]:
            dic_c = {}
            for c in keys[2]:
                dic_d = {}
                for d in keys[3]:
                    dic_d[d] = []
                dic_c[c] = dic_d
            dic_b[b] = dic_c
        dic[a] = dic_b

    info_list = list(map(lambda x: x.split(), info_list))
    info_list.sort()
    query_list = list(map(lambda x: list(filter(lambda y: y != "and", x.split())), query_list))

    for info in info_list:
        dic[info[0]][info[1]][info[2]][info[3]].append(info[4])

    # print(dic)
    for query in query_list:
        re = DFS(dic, query, 0, keys)
        answer.append(re)

    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])
