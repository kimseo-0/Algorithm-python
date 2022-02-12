import sys
input = sys.stdin.readline

N = int(input())
product_list = set(map(int, input().split()))
# set() : 집합 자료형 초기화
# 단순히 특정한 데이터가 존재하는지 검사할 때에 매우 효과적
# list() > O(N) : index 순서대로 탐색
# set()  > O(1) : hash function 을 통해
# index =  hash function (key) % hash table size 로 바로 값을 탐색 가능

M = int(input())
order_list = list(map(int, input().split()))

for order in order_list:
    if order in product_list:
        print('yes', end=" ")
    else:
        print('no', end=" ")