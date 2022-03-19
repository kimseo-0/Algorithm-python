from itertools import combinations

# combination
data_list = [1, 2, 3, 4, 5, 6]
N = 2
combination_list = list(combinations(data_list, N))
print('combination : ', combination_list)

# sort
data_list = [3, 2, 4, 6, 1, 5]
data_list.sort()
print(data_list)
data_list.sort(reverse=True)
print(data_list)
data_list.sort(key=lambda x: -x)
print(data_list)

data_list = [(3, 'c'), (2, 'b'), (4, 'a'), (3, 'a'), (1, 'c'), (5, 'b')]
data_list.sort(key=lambda x: (x[1], x[0]))
print(data_list)
