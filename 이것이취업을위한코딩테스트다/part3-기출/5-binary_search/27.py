# 정렬된 배열에서 특정 수의 개수 구하기
# O(logN) 으로 구현할 것
# 이진탐색을 활용하여 갯수를 세는 방법

def binary_search_first(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == X:
        if mid == 0 or array[mid - 1] < X:
            return mid
        else:
            return binary_search_first(array, start, mid - 1)
    elif array[mid] < X:
        return binary_search_first(array, mid + 1, end)
    else:
        return binary_search_first(array, start, mid - 1)

def binary_search_last(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == X:
        if mid == N - 1 or array[mid + 1] > X:
            return mid
        else:
            return binary_search_last(array, mid + 1, end)
    elif array[mid] < X:
        return binary_search_last(array, mid + 1, end)
    else:
        return binary_search_last(array, start, mid - 1)


N, X = map(int, input().split())
num_list = list(map(int, input().split()))
start = 0
end = N - 1
start = binary_search_first(num_list, start, end)
if start is None:
    print(0)
else:
    end = binary_search_last(num_list, start, end)
    print(end - start + 1)

# 7 2
# 1 1 2 2 2 2 3
