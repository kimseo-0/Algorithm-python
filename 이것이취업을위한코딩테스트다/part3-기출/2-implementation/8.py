import sys
input = sys.stdin.readline

alphabet_and_num = list(input())
alphabet = []
num = 0
for i in alphabet_and_num:
    if ('0' <= i) and (i <= '9'):
        num += int(i)
    else:
        alphabet.append(i)

alphabet.sort()
print(*alphabet, num, sep='')


# K2DA3K5
# > ADKK10

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
