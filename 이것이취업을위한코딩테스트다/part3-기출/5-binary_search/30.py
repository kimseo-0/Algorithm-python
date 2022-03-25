# 가사 검색
import sys
input = sys.stdin.readline

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "???me", '?????']

def check_match(word, querie):
    if len(word) < len(querie):
        return -1
    elif len(word) > len(querie):
        return 1

    for i in range(len(querie)):
        if querie[i] == "?":
            continue
        else:
            if word[i] < querie[i]:
                return -1
            elif word[i] > querie[i]:
                return 1
    return 0

def binary_search_first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    check = check_match(array[mid], target)
    if check == 0:
        if mid == 0 or check_match(array[mid - 1], target) != 0:
            return mid
        else:
            return binary_search_first(array, target, start, mid - 1)

    elif check < 0:
        return binary_search_first(array, target, mid + 1, end)
    else:
        return binary_search_first(array, target, start, mid - 1)

def binary_search_last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    check = check_match(array[mid], target)
    if check == 0:
        if (mid == (len(array) - 1)) or check_match(array[mid + 1], target) != 0:
            return mid
        else:
            return binary_search_last(array, target, mid + 1, end)

    elif check < 0:
        return binary_search_last(array, target, mid + 1, end)
    else:
        return binary_search_last(array, target, start, mid - 1)

def solution(words, queries):
    words_original = sorted(list(set(words)), key=lambda x: (len(x), x))
    words_reverse = sorted([word[::-1] for word in words], key=lambda x: (len(x), x))

    result = []

    for querie in queries:
        if querie[0] == '?':
            words = words_reverse
            querie = querie[::-1]
        else:
            words = words_original

        first = binary_search_first(words, querie, 0, len(words) - 1)
        if first is None:
            result.append(0)
            continue
        else:
            last = binary_search_last(words, querie, 0, len(words) - 1)
            result.append(last - first + 1)

    return result


print(solution(words, queries))
