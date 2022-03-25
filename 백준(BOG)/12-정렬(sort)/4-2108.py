import collections

N = int(input())
data_list = []
count_list = [0] * 8001

for i in range(N):
    num = int(input())
    data_list.append(num)
    count_list[num + 4000] += 1

data_list.sort()

# 평균
print(round(float(sum(data_list))/N))
# 중앙값
print(data_list[N//2])

# 최빈값
# index = count_list.index(max(count_list))
# if count_list.count(max(count_list)) == 1:
#     print(index - 4000)
# else:
#     print(count_list[index + 1:].index(max(count_list)) + index + 1 - 4000)


q = collections.Counter(data_list).most_common(2)
print(q)
print(q[q[0][1] == q[1][1]][0])

# 범위
print(max(data_list) - min(data_list))
