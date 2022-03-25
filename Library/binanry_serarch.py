def recursive_binary_search(array, target, start, end):
    if start > end:
        return

    # mid 를 구하는 과정이 수정될 수 있음
    mid = (start + end) // 2

    # 비교방법이 수정될 수 있음
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        recursive_binary_search(array, target, start, mid - 1)
    else:
        recursive_binary_search(array, target, mid + 1, end)


def loop_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
