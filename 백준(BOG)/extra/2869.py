import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

count = (V - A) // (A - B) + 1
move_distance = (V - A) % (A - B)

# print(count)
# print(V - move_distance)

while True:
    if move_distance <= 0:
        break
    move_distance -= (A - B)
    count += 1

print(count)
