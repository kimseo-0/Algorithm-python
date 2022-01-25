import sys
input = sys.stdin.readline

N = int(input())
student_list = []
for i in range(N):
    student = input().split()
    student_list.append([student[0], int(student[1])])

student_list.sort(key=lambda x: x[1])

for student in student_list:
    print(student[0], end=" ")
