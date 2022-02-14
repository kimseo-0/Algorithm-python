# 완전 탐색 알고리즘
card_num, max_num = map(int, input().split())

card = input().split()
card = list(map(int, input().split()))
#card = list(input().split())
#for i in range(card_num):
#    card[i] = int(card[i])


max_result = 0
for i in range(card_num):
    if card[i] >= max_num:
        continue
    for j in range(card_num):
        if i == j or card[i] + card[j] >= max_num:
            continue
        for k in range(card_num):
            if i == k or j == k:
                continue
            sum_num = card[i]+card[j]+card[k]
            if (sum_num <= max_num) and (sum_num > max_result):
                max_result = sum_num

print(max_result)

# 순열 문제를 조합으로 표현하자 
