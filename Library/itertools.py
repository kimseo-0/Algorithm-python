from bisect import bisect_left, bisect_right
from itertools import combinations

# combination
print('# combination')
data_list = [1, 2, 3, 4, 5, 6]
N = 2
combination_list = list(combinations(data_list, N))
print('combination : ', combination_list)
print()

# sort
print('# sort')
data_list = [3, 2, 4, 6, 1, 5]
data_list.sort()    # O(N logN)
print(data_list)
data_list.sort(reverse=True)
print(data_list)
data_list.sort(key=lambda x: -x)
print(data_list)

data_list = [(3, 'c'), (2, 'b'), (4, 'a'), (3, 'a'), (1, 'c'), (5, 'b')]
data_list.sort(key=lambda x: (x[1], x[0]))
print(data_list)
print()

# bisect
print('# bisect')
data_list = [1, 2, 3, 4, 4, 7]
print('data : ', data_list)
print('left index : ', bisect_left(data_list, 4))   # O(logN)
print('right index: ', bisect_right(data_list, 4))

# array 에서 범위가 left_value <= x <= right_value 인 데이터의 갯수 반환 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index - left_index


print('count 3~5 : ', count_by_range(data_list, 3, 5))
