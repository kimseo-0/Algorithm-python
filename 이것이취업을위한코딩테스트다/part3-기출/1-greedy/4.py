import sys
input = sys.stdin.readline

N = int(input())
money_type_list = list(map(int, input().split()))
money_type_list.sort(reverse=True)

min_money = 1
while True:
    money = min_money
    for money_type in money_type_list:
        if money >= money_type:
            money -= money_type

    if money == 0:
        min_money += 1
    else:
        break

print(min_money)




