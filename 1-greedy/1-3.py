# 1차 풀이 - 정답
N, M = map(int, input().split())
min_card_list = []

for i in range(N):
    card_row = list(map(int, input().split()))
    min_card_list.append(min(card_row))     # 행에서 가장 작은 숫자의 카드만을 추가

print(max(min_card_list))   # 가장 작은 숫자의 카드들 중 가장 큰 카드 찾기

# 2차 풀이 - 정답(책 참고)
N, M = map(int, input().split())

result = 0
for i in range(N):
    card_row = list(map(int, input().split()))

    result = max(result, min(card_row))

print(result)   # 가장 작은 숫자의 카드들 중 가장 큰 카드 찾기

'''
ex1
3 3
3 1 2
4 1 4
2 2 2
>> 2

ex2
2 4
7 3 1 8
3 3 3 4

>> 3
'''
