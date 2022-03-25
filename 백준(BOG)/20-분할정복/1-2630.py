N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

count_color = [0, 0]

def check_same(matrix, n):
    if n == 1:
        count_color[matrix[0][0]] += 1
        return

    if sum(list(map(sum, matrix))) == 0:
        count_color[0] += 1
        return
    if sum(list(map(sum, matrix))) == n * n:
        count_color[1] += 1
        return

    check_same([[y for y in x[:n//2]] for x in matrix[:n//2]], n//2)
    check_same([[y for y in x[n//2:]] for x in matrix[:n//2]], n//2)
    check_same([[y for y in x[:n//2]] for x in matrix[n//2:]], n//2)
    check_same([[y for y in x[n//2:]] for x in matrix[n//2:]], n//2)


check_same(board, N)
for i in count_color:
    print(i)
