import sys
input = sys.stdin.readline

def rotation_key(key):
    new_key = []
    for i in range(len(key)):
        row = []
        for j in range(len(key)):
            row.insert(0, key[j][i])
        print(row)
        new_key.append(row)
    return new_key

def padding_key(key, M, N):
    for i in range(M):
        key[i] = [*([0]*(N - 1)), *key[i], *([0]*(N - 1))]
    for i in range(N - 1):
        key.insert(0, [0] * (M + (N - 1) * 2))
        key.append([0] * (M + (N - 1) * 2))

def solution(key, lock):
    answer = True

    M = len(key)
    N = len(lock)

    padding_key(key, M, N)

    flag = True
    for r in range(4):
        for mx in range(M + N - 1):
            for my in range(M + N - 1):
                flag = True
                print(mx, my)
                for i in range(N):
                    for j in range(N):
                        print((i, j), (i + mx, j + my), lock[i][j] != key[i + mx][j + my])

                        if lock[i][j] == key[i + mx][j + my]:
                            flag = False
                            break

                    if not flag:
                        break

                if flag:
                    break
            if flag:
                break
        if flag:
            break

        key = rotation_key(key)

    answer = flag
    return answer


key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

for k in key:
    print(k)
# rotation_key(key)
solution(key, lock)