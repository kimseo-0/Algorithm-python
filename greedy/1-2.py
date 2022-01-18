N, M, K = map(int, input().split())
Num = list(map(int, input().split()))

Num.sort(reverse=True)
max_sum = 0     # 결과
point = 0       # 배열의 현재 포인트
count = K       # 하나의 숫자를 몇 번 반복

for i in range(M):
    if count == 0:
        if point != 0:
            if Num[point] == Num[point-1]:
                count = K
                point += 1
            else:
                point -= 1
                count = K
        else:
            point += 1
            if Num[point] == Num[point - 1]:
                count = K
            else:
                count = 1
    max_sum += Num[point]
    print(Num[point])
    count -= 1

print(Num)
print(max_sum)

# 문제를 이해하는 시간을 더 가진다.
