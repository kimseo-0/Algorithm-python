# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
value_list = []
for i in range(N):
    value_list.insert(0, int(input()))

count = 0
for value in value_list:
    if K >= value:
        count += K // value
        K = K % value

print(count)