import heapq

# 최소 힙
def heap_min_sort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

# 최대 힙
def heap_max_sort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result
