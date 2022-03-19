
def count_sort(array):
    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    result = []
    for i in range(1, len(count)):
        for j in range(count[i]):
            result.append(i)

    return result


print(count_sort([7, 3, 1, 2, 4, 5, 2, 0, 9, 5]))
