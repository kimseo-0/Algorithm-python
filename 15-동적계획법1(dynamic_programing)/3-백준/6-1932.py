N = int(input())
triangle = []
for i in range(N):
    triangle.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
        else:
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

print(max(triangle[-1]))
