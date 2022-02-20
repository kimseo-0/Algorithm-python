import sys
input = sys.stdin.readline

S = list(input().strip())

zero = 0
one = 0
if S[0] == "0":
    zero += 1
else:
    one += 1

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        if S[i] == "0":
            zero += 1
        else:
            one += 1

print(min(zero, one))


binary = [0, 0]
binary[int(S[0])] += 1

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        binary[int(S[i])] += 1

print(min(binary))
