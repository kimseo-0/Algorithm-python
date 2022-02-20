def solution(N, stages):
    users = [0] * (N + 2)
    for i in range(len(stages)):
        users[stages[i]] += 1

    answer = [i for i in range(1, N + 1)]   # [1, 2, 3, 4, 5] [1, 2,....,N - 1, N]
    answer.sort(key=lambda x: -(users[x]/sum(users[x:])) if sum(users[x:]) != 0 else 0)
    return answer


# stages : [2, 1, 2, 6, 2, 4, 3, 3]
# users  : [0, 1, 3, 2, 1, 0, 1]
# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])













def solution2(N, stages):
    result = [0] * (N + 1)
    answer = [i for i in range(1, N + 1)]
    all_challenger = len(stages)
    for i in range(1, N + 1):
        if all_challenger != 0:
            fail_users = stages.count(i)
            result[i] = fail_users/all_challenger
            all_challenger -= fail_users

    answer.sort(key=lambda x: -result[x])
    return answer

solution2(5, [2, 1, 2, 6, 2, 4, 3, 3])

def solution3(N, stages):
    result = {}
    all_challenger = len(stages)
    for stage in range(1, N+1):
        if all_challenger != 0:
            count = stages.count(stage)
            result[stage] = count / all_challenger
            all_challenger -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

print(solution3(5, [2, 1, 2, 6, 2, 4, 3, 3]))
