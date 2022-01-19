import sys
input = sys.stdin.readline

# N = int(input())
# plan = list(input().split())
N = 5
plan = ["R", "R", "R", "U", "D", "D"]

x = 1
y = 1
for i in plan:
    if i == "L":
        x = 1 if (x == 1) else x - 1
    elif i == "R":
        x = N if (x == N) else x + 1
    elif i == "U":
        y = 1 if (y == 1) else y - 1
    elif i == "D":
        y = N if (y == N) else y + 1

    # if x < 1:
    #     x = 1
    # elif x > N:
    #     x = N
    # if y < 1:
    #     y = 1
    # elif y > N:
    #     y = N

print(x, y)
