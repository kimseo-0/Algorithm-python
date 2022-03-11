game_list = [[0] * 3 for _ in range(3)]
result = ""
index = 0
while True:
    line = input()
    if line == 'end':
        break
    num_X = 0
    num_O = 0
    for i in range(3):
        for j in range(3):
            game_list[i][j] = line[i * 3 + j]
            if game_list[i][j] == 'O':
                num_O += 1
            elif game_list[i][j] == 'X':
                num_X += 1

    # 문제 조건상 X 가 먼저 이므로 무조건 X의 갯수가 O보다 많아야하고,
    # 번갈아 가며 플레이 하므로 둘의 차이가 1 또는 0 이어야 함
    if num_X - num_O != 0 and num_X - num_O != 1:
        result += "invalid\n"
        continue

    score = ['.'] * 8
    for i in range(3):
        if game_list[i][0] == game_list[i][1] and game_list[i][1] == game_list[i][2]:
            score[i] = game_list[i][0]
        if game_list[0][i] == game_list[1][i] and game_list[1][i] == game_list[2][i]:
            score[3 + i] = game_list[0][i]
    if game_list[0][0] == game_list[1][1] and game_list[1][1] == game_list[2][2]:
        score[6] = game_list[1][1]
    if game_list[0][2] == game_list[1][1] and game_list[1][1] == game_list[2][0]:
        score[7] = game_list[1][1]

    success_X = score.count('X')
    success_O = score.count('O')
    # print(index, score)
    # 성공 갯수 0개 > 게임판이 가득 찬 경우
    if success_X + success_O == 0:
        if num_X + num_O == 9:
            result += "valid\n"
        else:
            result += "invalid\n"
    # 성공 갯수 1개
    elif success_X + success_O == 1:
        # O 가 이긴 경우
        if num_X - num_O == 0:
            if success_O == 1:
                result += "valid\n"
                continue
        # X 가 이긴 경우
        elif num_X - num_O == 1:
            if success_X == 1:
                result += "valid\n"
                continue
        result += "invalid\n"
    # 성공 갯수 2개 이상
    # 성공이 모두 동일한 사람이어야 하며, 마지막 하나의 칸으로 여러개가 성공이 될 수 있어야함
    # 해당 상황에서는 X만 가능하다.
    else:
        if success_X > 0 and success_O > 0:
            result += "invalid\n"
        # X 가 이긴 경우
        elif success_X > 0:
            if num_X - num_O == 1:
                result += "valid\n"
                continue
            result += "invalid\n"
        # O 가 이긴 경우 > 이런 경우는 없다
        else:
            result += "invalid\n"

print(result)
