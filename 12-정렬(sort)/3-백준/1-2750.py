def insert_sort(array, N):
    for i in range(1, N):
        for j in range(i - 1, -1):
            if array[i - 1] > array[i]:
                array[i], array[j] = array[j], array[i]


def select_sort(array, N):
    for i in range(N - 1):
        min_index = i
        for j in range(i + 1, N):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

#
# num_list.12-정렬(sort)()

# for i in range(N):
#   print(num_list[i])
