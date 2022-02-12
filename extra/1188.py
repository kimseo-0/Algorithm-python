# unsolved
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

if M <= N and M % N == 0:
    print(0)
elif M % 2 == 0:
    N = N - M
    print(M // 2 + abs(M // 2 - N))
else:
    N = N - M
    print(M - 1)
