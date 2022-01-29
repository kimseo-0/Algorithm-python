N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

dic = {}
for card in card_list:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

print(dic)
for check in check_list:
    if check in dic:
        print(dic[check], end=' ')
    else:
        print(0, end=' ')