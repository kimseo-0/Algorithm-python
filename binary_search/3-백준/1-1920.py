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


N = int(input())
answer_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

answer_list.sort()
for check_num in check_list:
    if binary_search(answer_list, check_num, 0, N - 1) is None:
        print(0)
    else:
        print(1)


# 정렬 >  O(N logN)
# 이진 탐색 > O(log N)

