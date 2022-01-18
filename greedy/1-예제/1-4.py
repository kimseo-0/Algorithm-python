# 1차 풀이
# 1. N에 -1을 하는 것
# 2. N을 K로 나누는 것
# 두가지 방법 중 2번이 1번보다 더 빠르게 N을 1로 도달하게 한다
N, K = map(int, input().split())

count = 0
while N > 1:
    if N % K == 0:
        N = N // K
    else:
        N -= 1
    count += 1

print(count)

# 2차 풀이
# N < K 되는 순간부터 위 방법중 2번 방법은 사용할 수 없다는것이 명확하다.
# N < K 가 되는 순간 N % K == 0이 성립하지 않기 때문이다.
# 해당 조건을 추가하면 연산 수를 줄일 수 있다.

N, K = map(int, input().split())

count = 0
while N >= K:
    if N % K == 0:
        N = N // K
    else:
        N -= 1
    count += 1

count += (N - 1)
print(count)
