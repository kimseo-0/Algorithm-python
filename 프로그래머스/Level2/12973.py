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

def check1(s, start, end):
    print(start, end)
    if start + 1 == end:
        if s[start] == s[end]:
            return 1
        else:
            return 0

    if (end - start + 1) % 2 == 1:
        return 0

    mid = s.find(s[start], start + 1, end + 1)
    print(s[start], mid)
    if mid == -1:
        return 0

    if start + 1 == mid:
        if s[start] == s[mid]:
            return 1
        else:
            return 0
    elif mid == len(s) - 1:
        return check1(s, start + 1, mid - 1)
    else:
        return check1(s, start + 1, mid - 1) and check1(s, mid + 1, end)


def check2(s, start, end):
    if (start - end + 1) % 2 == 1:
        return 0

    if start + 1 == end:
        return 1

    start += 1
    end -= 1
    print(start, end)
    while start < end:
        next_end = len(s) - s[::-1].find(s[start], len(s) - end - 1, len(s) - start) - 1
        print(s[::-1], len(s) - end - 1, len(s) - start, next_end)
        if next_end == len(s) or not check2(s, start, next_end):
            return 0
        start = next_end + 1

    return 1

def solution(s):
    if len(s) % 2 == 1:
        return 0

    start = -1
    end = len(s)

    return check2(s, start, end)


# print(solution("babbab"))
# print(solution("aabbcbbc"))
print(solution("abab"))
# print(solution("aaabbaaabaabbaab"))
# print(solution("ac"))
# print(solution("abba"))