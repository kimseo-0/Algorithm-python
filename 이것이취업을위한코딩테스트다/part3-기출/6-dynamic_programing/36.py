import sys
from copy import deepcopy
input = sys.stdin.readline

# DFS 를 활용한 풀이 > 시간초과 발생
def DFS(word, index, count):
    # print(word)
    if index >= len(correct) or index >= len(word):
        return count + abs(len(correct) - len(word))

    if word[index] == correct[index]:
        count = DFS(word, index + 1, count)
        return count
    else:
        new_word = deepcopy(word)
        new_word.insert(index, correct[index])
        # print('insert')
        insert_count = DFS(new_word, index + 1, count + 1)

        new_word = deepcopy(word)
        new_word.pop(index)
        # print('remove')
        remove_count = DFS(new_word, index, count + 1)

        new_word = deepcopy(word)
        new_word[index] = correct[index]
        # print('replace')
        replace_count = DFS(new_word, index + 1, count + 1)

        return min(insert_count, remove_count, replace_count)


original = list(input().strip())
correct = list(input().strip())

print(DFS(original, 0, 0))


# DP 테이블을 활용한 풀이
N = len(correct)
M = len(original)
DP = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, N + 1):
    DP[0][i] = i
for i in range(1, M + 1):
    DP[i][0] = i

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if correct[j - 1] == original[i - 1]:
            DP[i][j] = DP[i - 1][j - 1]
        else:
            DP[i][j] = min(DP[i - 1][j - 1], DP[i - 1][j], DP[i][j - 1]) + 1

print(DP[M][N])
