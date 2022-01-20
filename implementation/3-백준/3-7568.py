import sys
input = sys.stdin.readline

N = int(input())
people = []

for i in range(N):
    people_row = list(map(int, input().split()))
    people_row.append(i)
    people.append(people_row)

for i in range(len(people)):
    count = 1
    for j in range(len(people)):
        if i == j:
            continue
        elif (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
            count += 1

    print(count, end=" ")

# 이 문제를 5번이나 시도 했는데
# 이유는 문제 조건상
# a의 몸무게 < b의 몸무게 and a의 키 < b의 키 일때 b가 a보다 덩치가 크다라고
# 제시되어있음에도 불구하고 a와 b의 몸무게 또는 키가 같을 때를 고려 했다.
