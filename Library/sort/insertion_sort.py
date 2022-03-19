
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


print(insertion_sort([7, 3, 1, 2, 4, 5, 2, 0, 9, 5]))
