
def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    return array

def quick_sort_2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort_2(left) + [pivot] + quick_sort_2(right)


print(quick_sort([7, 3, 1, 2, 4, 5, 2, 0, 9, 5], 0, 9))
print(quick_sort_2([7, 3, 1, 2, 4, 5, 2, 0, 9, 5]))

