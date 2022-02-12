import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# python return 값 없으면, 기본적으로 None return 한다.

N = int(input())
product_list = list(map(int, input().split()))
M = int(input())
order_list = list(map(int, input().split()))

product_list.sort()
for order in order_list:
    result = binary_search(product_list, order, 0, N - 1)

    if result is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
