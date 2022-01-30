N, M = map(int, input().split())
money_list = []
for i in range(N):
    money_list.append(int(input()))

# money_list.sort()

DP = [0] * (M + 1)

for i in range(1, M + 1):
    DP[i] = -1  # 기본적으로 만들 수 없는 화폐로 지정
    for money in money_list:    # 모든 화폐 단위에 대해서 확인
        if not ((i - money) < 0 or DP[i - money] == -1):
            # (해당 화폐단위로 뺄 수 없거나, 해당 주화로 뺐을때 더이상 만들 수 없는 화폐가 되는 경우가) 아닐때,
            # 즉, 해당 화폐 단위로 뺐을 때 만들 수 있는 화폐일 때
            if DP[i] != -1:
                DP[i] = min(DP[i - money] + 1, DP[i])
            else:
                DP[i] = DP[i - money] + 1

print(DP)
print(DP[M])
