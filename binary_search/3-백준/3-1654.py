import sys
input = sys.stdin.readline

def binary_search(array, start, end, result):
    if start > end:
        return result
    mid = (start + end) // 2
    sum_of_result = 0
    for i in array:
        sum_of_result += i // mid
    if sum_of_result < M:
        return binary_search(array, start, mid - 1, result)
    else:
        result = mid
        return binary_search(array, mid + 1, end, result)


N, M = map(int, input().split())
line_list = []
for i in range(N):
    line_list.append(int(input()))

length = 0
line_list.sort()
length = binary_search(line_list, 1, line_list[-1], length)

print(length)

