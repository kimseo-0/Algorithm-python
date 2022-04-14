# 다단계 칫솔 판매
# https://programmers.co.kr/learn/courses/30/lessons/77486
from collections import deque


def solution(enroll, referral, seller, amount):
    answer = []

    money = {}
    tree = {}
    for i in range(len(enroll)):
        money[enroll[i]] = 0
        tree[enroll[i]] = referral[i]

    # print(tree)
    for i in range(len(seller)):
        node = seller[i]
        new_money = amount[i] * 100
        while True:
            # print(node)
            if new_money == 0:
                break

            temp_money = int(new_money * 10 / 100)
            money[node] += new_money - temp_money

            node = tree[node]
            new_money = temp_money

            if node == '-':
                break

    # print(money)
    answer = list(money.values())
    # print(answer)
    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])
