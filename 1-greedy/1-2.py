N, M, K = map(int, input().split())
Num = list(map(int, input().split()))

Num.sort(reverse=True)  # 리스트의 큰 수들을 먼저 더해주기 위해 정렬 후 reverse 했다.
max_sum = 0     # 결과
point = 0       # 배열의 현재 포인트
count = K       # 하나의 숫자를 몇 번 반복

for i in range(M):  # M번 더하는 작업을 반복함
    if count == 0:  # count가 0이되면 count를 K 또는 1로 수정하는 작업
        if point != 0:  # point가 0이면 point-1로 갈 수 없기 때문에 예외처리
            '''
            여기 코드부터는 완전히 잘못된 생각 및 풀이입니다
            기본적으로 문제 자체를 
            인풋값이 6 6 5 4 일때
            666 666 5 666 이런식으로 풀어야한다고 이해함
            '''
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

    # 공통적으로 수행하는 부분
    max_sum += Num[point]
    count -= 1  # 한번 더할 때마다, count를 감소

print(max_sum)

# 문제를 이해하는 시간을 더 가진다.
