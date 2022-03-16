# 만들 수 없는 동전
# 목적 : 만들 수 없는 금액 찾기
# 현재 상태 : 1부터 1 - target 까지의 모든 금액을 만들 수 있는 상태
# 그리디 기준 : 화폐 단위가 작은 동전부터

import sys
input = sys.stdin.readline

N = int(input())
money_type_list = list(map(int, input().split()))

money_type_list.sort()

# min_money - 1 까지 만들 수 있음
min_money = 1
for money_type in money_type_list:
    if min_money < money_type:
        break

    # min_money + 1, min_money + 2 .... , min_money + (min_money - 1) 까지 만들 수 있다.
    min_money += money_type

print(min_money)


# money_type_list.sort(reverse=True)
# min_money = 1
# while True:
#     money = min_money
#     for money_type in money_type_list:
#         if money >= money_type:
#             money -= money_type
#
#     if money == 0:
#         min_money += 1
#     else:
#         break
#
# print(min_money)

#

