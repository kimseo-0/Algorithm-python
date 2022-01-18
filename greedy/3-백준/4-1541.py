import sys
input = sys.stdin.readline
argument = input().split("-")

result = sum(map(int, argument[0].split("+")))
for i in range(1, len(argument)):
    result -= sum(map(int, argument[i].split("+")))
print(result)
