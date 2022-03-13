def solution(n, weak, dist):
    answer = 0
    weak_dist_right = [[0] * len(weak) for _ in range(len(weak))]
    weak_dist_left = [[0] * len(weak) for _ in range(len(weak))]
    for i in range(len(weak)):
        for j in range(len(weak)):
            if i <= j:
                weak_dist_right[i][j] = abs(weak[j] - weak[i])
                weak_dist_left[j][i] = abs(weak[j] - weak[i])
            else:
                weak_dist_right[i][j] = abs(n - weak[i] + weak[j])
                weak_dist_left[j][i] = abs(n - weak[i] + weak[j])

    print(weak_dist_right)
    print(weak_dist_left)
    dist.sort(reverse=True)
    min_count = len(dist)
    people_count = 0
    weak_count = len(weak) - 1
    while weak_count < len(weak):
        if weak_dist_right[i][(i + j) % len(weak)] <= dist[people_count]:
            weak_count -= 1



    dist.sort(reverse=True)

    return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])

# 3 4 1 4
