import sys
input = sys.stdin.readline

N, K = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

list_A.sort()
list_B.sort(reverse=True)

for i in range(K):
    if list_A[i] < list_B[i]:
        list_A[i], list_B[i] = list_B[i], list_A[i]
    else:
        break

print(sum(list_A))

# '최대 K번'
