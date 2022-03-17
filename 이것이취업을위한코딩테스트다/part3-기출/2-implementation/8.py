# 문자 재정렬
# 알파벳인 경우 순서대로
# 숫자인 경우 알파벳 출력 뒤에 붙여서 출력 > "숫자가 없는 경우?"

import sys
input = sys.stdin.readline

# solution 1
# alphabet_and_num = list(input())
# alphabet = []
# num = 0
# for i in alphabet_and_num:
#     if ('0' <= i) and (i <= '9'):
#         num += int(i)
#     else:
#         alphabet.append(i)
#
# alphabet.sort()
# print(*alphabet, num, sep='')

# K2DA3K5
# > ADKK10

# solution 2
# 아스키코드 활용
# 파이썬에서는 아스키코드 변환 없이
# 같은 타입의 경우 비교연산자로 아스키코드로 비교 가능
# alphabet_and_num = list(map(ord, list(input())))
# alphabet = []
# num = 0
# for i in alphabet_and_num:
#     if (ord('0') <= i) and (i <= ord('9')):
#         num += int(chr(i))
#     else:
#         alphabet.append(chr(i))
#
# alphabet.sort()
# print(*alphabet, num, sep='')

# solution 3
# 위에서 제시한 솔루션은 숫자가 하나도 없을 때를 고려하지 않았음
# 원인은, 주어진 테스트 케이스에 해당 내용이 없었고, 문제 자체에서도 언급되지 않았기 때문
# 항상 입력 값에 대한 극단적인 케이스를 생각해보고 적용할 필요가 있다.
alphabet_and_num = list(input().strip())
result = []
num = 0
for data in alphabet_and_num:
    if data.isalpha():
        result.append(data)
    else:
        num += int(data)

if num != 0:
    result.append(str(num))

print(''.join(result))
