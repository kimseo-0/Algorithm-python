import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

count_color = [0, 0, 0]

def check_same(matrix, n):
    if n == 1:
        count_color[matrix[0][0]] += 1
        return

    if sum(list(map(lambda x: x.count(-1), matrix))) == n * n:
        count_color[-1] += 1
        return
    elif sum(list(map(lambda x: x.count(0), matrix))) == n * n:
        count_color[0] += 1
        return
    elif sum(list(map(lambda x: x.count(1), matrix))) == n * n:
        count_color[1] += 1
        return

    check_same([[y for y in x[:n // 3]] for x in matrix[:n//3]], n//3)
    check_same([[y for y in x[n // 3:2 * n//3]] for x in matrix[:n//3]], n//3)
    check_same([[y for y in x[2 * n//3:]] for x in matrix[:n//3]], n//3)

    check_same([[y for y in x[:n // 3]] for x in matrix[n // 3:2 * n//3]], n // 3)
    check_same([[y for y in x[n // 3:2 * n // 3]] for x in matrix[n // 3:2 * n//3]], n // 3)
    check_same([[y for y in x[2 * n // 3:]] for x in matrix[n // 3:2 * n//3]], n // 3)

    check_same([[y for y in x[:n // 3]] for x in matrix[2 * n // 3:]], n // 3)
    check_same([[y for y in x[n // 3:2 * n // 3]] for x in matrix[2 * n // 3:]], n // 3)
    check_same([[y for y in x[2 * n // 3:]] for x in matrix[2 * n // 3:]], n // 3)


check_same(board, N)
print(count_color[-1])
print(count_color[0])
print(count_color[1])
