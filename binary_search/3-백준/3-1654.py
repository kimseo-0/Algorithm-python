import sys
input = sys.stdin.readline

def binary_search(array, start, end):
    result = 0
    result_mid = (start + end) // 2
    while start < end:
        mid = (start + end) // 2
        left = array[mid] - array[start]
        right = array[end] - array[mid]
        if left == right:
            result = left
            break
        elif left < right:
            if result < left:
                result = left
                result_mid = mid
            start += 1
        else:
            if result < right:
                result = right
                result_mid = mid
            end -= 1
        print(left, right, result)
    return result, result_mid


N, M = map(int, input().split())
house_list = []
for i in range(N):
    house_list.append(int(input()))

house_list.sort()

# for i in range(2, M):
