N = int(input())
food_list = list(map(int, input().split()))

DP = [0] * N

DP[0] = food_list[0]   # 0번째 창고를 털었을 때, 1번째 x
DP[1] = max(food_list[0] + 0, 0 + food_list[1])
# 1번재 창고를 터는게 좋을까? 안터는게 좋을까 확인해야해!

for i in range(2, N):
    DP[i] = max(DP[i - 2] + food_list[i], DP[i - 1])    # i번째 창고 털까? 말까?

print(DP[N-1])  # print(max(DP[N-1], DP[N-2]))
# 이미 위의 점화식에서 계산 N-1번째 창고에 대한 최댓값을 계산 했기 때문에 다시 비교할 필요가 없다
# print(DP)
