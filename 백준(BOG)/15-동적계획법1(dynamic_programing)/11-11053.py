# unsolved
N = int(input())
num_list = list(map(int, input().split()))

result = [[1, num_list[0]]]

for i in range(N):
    for j in range(len(result)):
        if result[j][1] < num_list[i]:
            result[j][0] += 1
            result[j][1] = num_list[i]
        else:
            result.append([1, num_list[i]])

print(result)
