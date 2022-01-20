import sys
input = sys.stdin.readline

N = int(input())
people = []

for i in range(N):
    people_row = list(map(int, input().split()))
    people_row.append(i)
    people.append(people_row)

people.sort(reverse=True)

rank = [0] * N
rank[people[0][2]] = 1
prev_rank = 1
for i in range(1, len(people)):
    if people[i-1][0] == people[i][1]:
        if people[i - 1][1] > people[i][1]:
            prev_rank = i + 1
    else:
        if people[i-1][1] >= people[i][1]:
            prev_rank = i + 1
    rank[people[i][2]] = prev_rank

for i in rank:
    if i == N - 1:
        print(i)
    else:
        print(i, end=" ")

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# people = []
#
# for i in range(N):
#     people_row = list(map(int, input().split()))
#     people_row.append(i)
#     people.append(people_row)
#
# for i in range(len(people)):
#     count = 1
#     for j in range(len(people)):
#         if i == j:
#             continue
#         if (people[i][0] < people[j][0]) and (people[i][1] < people[i][j])
#
#     print(count, end=" ")
