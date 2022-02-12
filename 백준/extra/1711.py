import sys
input = sys.stdin.readline

N = int(input())
value_list = []
for i in range(N):
    x, y = map(int, input().split())
    value_list.append([x, y])
value_list.sort()

vector_mat = []
for i in range(N):
    #difference_row = []
    for j in range(i):
        vector_mat.append([value_list[i][0] - value_list[j][0], value_list[i][1] - value_list[j][1]])
    #vector_mat.append(difference_row)

print(vector_mat)
count = 0
# for i in range(N):
#     for j in range(0, i):
#         for k in range(j + 1, i):
#             if vector_mat[i][j][0]*vector_mat[i][k][0] + vector_mat[i][j][1] * vector_mat[i][k][1] == 0:
#                 print(i, j, k)
#                 count += 1

for i in range(len(vector_mat)):
    for j in range(i, len(vector_mat)):
        if (vector_mat[i][0] * vector_mat[j][0] + vector_mat[i][1] * vector_mat[j][1]) == 0:
            print(i, j)
            count += 1

print(count)
