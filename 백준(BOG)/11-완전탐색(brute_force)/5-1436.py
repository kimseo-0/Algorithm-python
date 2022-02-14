import sys
input = sys.stdin.readline

N = int(input())

i = 665
count = 0
while True:
    i += 1
    if str(i).find("666") != -1:
        count += 1
        if count >= N:
            break
print(i)
