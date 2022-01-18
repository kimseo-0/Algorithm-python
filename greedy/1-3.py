N, M = map(int, input().split())
min_card_list = []

for i in range(N):
    card_row = list(map(int, input().split()))
    min_card_list.append(min(card_row))

print(max(min_card_list))

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
