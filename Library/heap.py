import heapq

# 최소 힙 정렬
def heap_min_sort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

# 최대 힙 정렬
def heap_max_sort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


# 힙 생성
h = []
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 2)
print(h)

h2 = [1, 4, 2]
heapq.heapify(h2)
print(h2)

