# 배수와 약수
# https://www.acmicpc.net/problem/5086

import sys
input = sys.stdin.readline

'''
b가 a의 약수임을 확인하는 함수
'''
def check_factor(a, b):
    if a % b == 0:
        return True
    else:
        return False


'''
a가 b의 배수임을 확인하는 함수
'''
def check_multiple(a, b):
    if a % b == 0:
        return True
    else:
        return False


result = []
while True:
    first_num, second_num = map(int, input().split())

    if not (first_num and second_num):
        break

    if check_factor(second_num, first_num):
        result.append('factor')
    elif check_multiple(first_num, second_num):
        result.append('multiple')
    else:
        result.append('neither')

for i in result:
    print(i)
