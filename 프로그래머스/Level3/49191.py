def solution(n, results):
    answer = 0
    graph_win = [[] for _ in range(n + 1)]
    graph_lose = [[] for _ in range(n + 1)]
    for i in range(len(results)):
        [a, b] = results[i]
        graph_win[a].append(b)
        graph_lose[b].append(a)
        for j in range(1, n + 1):
            if a in graph_win[j] and b not in graph_win[j]:
                graph_win[j].append(b)
            if b in graph_lose[j] and b not in graph_lose[j]:
                graph_lose[j].append(a)
    print(graph_win)
    print(graph_lose)
    for i in range(1, n + 1):
        if len(graph_win[i]) + len(graph_lose[i]) == n - 1:
            answer += 1
    print(answer)
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
