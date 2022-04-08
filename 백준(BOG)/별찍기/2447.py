def print_star(n, index):
    if n == 1:
        return
    for i in range(3):
        for j in range(3):
            print_star(n//3, i, j)
            if i == 1 and j == 1:
                for a in range(n//3):
                    for b in range(n//3):
                        # print(i, j, a, b)
                        result[((i // 3) * (n // 3) + j) % N] += " "
            else:
                # print(j, n)
                print(i, j, n)
                result[((i // 3) * (n // 3) + j) % N] += "*"
            print(result)


N = int(input())
result = [""] * N
print_star(N, 0)
print(result)
for r in result:
    print(r)
