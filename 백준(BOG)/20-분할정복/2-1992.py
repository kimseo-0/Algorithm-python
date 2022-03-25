N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, list(input().strip()))))

count_color = [0, 0]

def check_same(matrix, n):
    if n == 1:
        print(matrix[0][0], end='')
        return

    if sum(list(map(sum, matrix))) == 0:
        print(0, end='')
        return
    if sum(list(map(sum, matrix))) == n * n:
        print(1, end='')
        return

    print('(', end='')
    check_same([[y for y in x[:n//2]] for x in matrix[:n//2]], n//2)
    check_same([[y for y in x[n//2:]] for x in matrix[:n//2]], n//2)
    check_same([[y for y in x[:n//2]] for x in matrix[n//2:]], n//2)
    check_same([[y for y in x[n//2:]] for x in matrix[n//2:]], n//2)
    print(')', end='')


check_same(board, N)
