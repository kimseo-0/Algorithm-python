# 고정점 찾기
# O(logN) 으로 구현할 것
# 08:25 - 08:35
# 고정점 : 값 == 인덱스
# 고정점은 최대 1개 존재
# 고정점이 없으면 -1

def binary_search(array, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)
    else:
        return binary_search(array, start, mid - 1)


N = int(input())
num_list = list(map(int, input().split()))
result = binary_search(num_list, 0, N - 1)
print(result)

# 5
# -15 -6 1 3 7
# > 3

# 7
# -1 0 1 2 3 4 5
# > -1
