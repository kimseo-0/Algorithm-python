def fibonacci_top_down(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]

    d[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
    return d[n]

def fibonacci_bottom_up(n):
    d = [0] * (n + 1)
    d[1] = 1
    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n]


N = int(input())
for i in range(1, N + 1):
    d = [0] * (i + 1)

    print(fibonacci_top_down(i), end=" ")
    print(fibonacci_bottom_up(i))

