# 럭키 스트레이트
# 절반 왼쪽의 자릿수의 합 == 절반 오른쪽 자릿수의 합 > LUCKY

N = list(map(int, list(input())))

# solution 1
# mid = len(N) // 2
# left = sum(N[:mid])
# right = sum(N[mid:])
#
# if left == right:
#     print("LUCKY")
# else:
#     print("READY")

# solution 2
mid = len(N) // 2
result = sum(N[:mid]) - sum(N[mid:])

if result == 0:
    print("LUCKY")
else:
    print("READY")


