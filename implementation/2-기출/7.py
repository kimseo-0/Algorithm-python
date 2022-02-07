N = list(map(int, list(input())))

mid = len(N) // 2
left = sum(N[:mid])
right = sum(N[mid:])

if left == right:
    print("LUCKY")
else:
    print("READY")
