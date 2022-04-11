# 2017 팁스타운 > 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    temp_s = ""
    temp = ""
    i = 0
    while True:
        while i < len(s):
            if i == len(s) - 1:
                if temp != s[i]:
                    temp_s += temp
                    temp = s[i]
                else:
                    temp = ""
                break
            if s[i] == s[i + 1]:
                i += 2
            else:
                if temp != s[i]:
                    temp_s += temp
                    temp = s[i]
                else:
                    temp = ""
                i += 1
        temp_s += temp
        if s == temp_s:
            return 0
        s = temp_s
        if s == "":
            return 1
        temp_s = ""
        temp = ""
        i = 0

def check(s, start, end):
    temp_start = start
    temp_end = end
    while start < end:
        if s[start] == s[start + 1]:
            start += 2
        if s[end] == s[end - 1]:
            end -= 2
        if start >= end:
            break
        if s[start] != s[start + 1] and s[end] != s[end - 1]:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                sub_end = s.find(s[start], start + 1, end)
                if sub_end == -1:
                    return 0
                sub_start = s.find(s[end], start, end - 1)
                if sub_start == -1:
                    return 0
                start = sub_end + 1
                end = sub_start - 1
                if sub_end > sub_start:
                    return 0
                else:
                    if not check(s, start, sub_end):
                        return 0
                    if not check(s, sub_start, end):
                        return 0

        if temp_start == start and temp_end == end:
            return 0

        temp_start = start
        temp_end = end
    return 1

def solution1(s):
    if len(s) % 2 == 1:
        return 0

    start = 0
    end = len(s) - 1

    return check(s, start, end)


print(solution1("baabaa"))
print(solution1("abbabbcbbc"))
print(solution1("abab"))
print(solution1("abba"))
