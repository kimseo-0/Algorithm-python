import sys
input = sys.stdin.readline


def rotation_key(key, key_len):
    new_key = []
    for i in range(key_len):
        row = []
        for j in range(key_len):
            row.insert(0, key[j][i])
        new_key.append(row)
    return new_key

def padding_key(key, key_len, lock_len):
    for i in range(key_len):
        key[i] = [*([0]*(lock_len - 1)), *key[i], *([0]*(lock_len - 1))]
    for i in range(lock_len - 1):
        key.insert(0, [0] * (key_len + (lock_len - 1) * 2))
        key.append([0] * (key_len + (lock_len - 1) * 2))

def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)

    padding_key(key, key_length, lock_length)

    flag = True
    # 4가지 종류의 key
    for r in range(4):

        # key 를 (mx, my) 만큼 이동
        for mx in range(key_length + lock_length - 1):
            for my in range(key_length + lock_length - 1):

                # key 와 lock 확인
                flag = True
                for i in range(lock_length):
                    for j in range(lock_length):
                        # 하나라도 맞지 않는다면 break
                        if lock[i][j] == key[i + mx][j + my]:
                            flag = False
                            break
                    # 하나라도 맞지 않는 상황이면 break
                    if not flag:
                        break

                # 모두 맞는 경우 더이상 key 를 확인할 필요가 없음
                if flag:
                    break
            # 모두 맞는 경우 더이상 key 를 확인할 필요가 없음
            if flag:
                break
        # 모두 맞는 경우 더이상 key 를 확인할 필요가 없음
        if flag:
            break

        key = rotation_key(key, key_length)

    return flag


answer_key = [[0, 0, 0], [1, 0, 0], [0,  1, 1]]
answer_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(answer_key, answer_lock)
