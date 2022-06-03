def check_four_block(n, m, board):
    result = []
    for i in range(n - 1):
        for j in range(m - 2, -1, -1):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i + 1][j] and board[i + 1][j] == board[i + 1][j + 1] and board[i + 1][j + 1] == board[i][j + 1]:
                result.extend([(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)])
    result = list(set(result))
    result.sort(key=lambda x: -x[1])
    return result

def solution(m, n, board):
    answer = 0

    new_board = [[0] * m for i in range(n)]
    for i in range(m):
        for j in range(n):
            new_board[j][m - 1 - i] = board[i][j]

    while True:
        for b in new_board:
            print(b)
        print()

        blocks = check_four_block(n, m, new_board)
        print(blocks)

        if len(blocks) == 0:
            break

        for (i, j) in blocks:
            answer += 1
            new_board[i].pop(j)
            new_board[i].append(0)

    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
