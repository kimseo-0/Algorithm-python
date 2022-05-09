# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3


def solution1(name):
    num = ord("Z") - ord("A") + 1
    right = 0
    left = 0

    count = 0
    for i in range(len(name)):
        print(min(ord(name[i]) - ord("A"), num - (ord(name[i]) - ord("A"))))
        right += min(ord(name[i]) - ord("A"), num - (ord(name[i]) - ord("A")))

        if i == len(name) - 1:
            break

        if name[i + 1] == 'A':
            count += 1
        else:
            right += count + 1
            count = 0

    count = 0
    for i in range(len(name)):
        left += min(ord(name[-i]) - ord("A"), num - (ord(name[-i]) - ord("A")))

        if i == len(name) - 1:
            break

        if name[-i - 1] == 'A':
            count += 1
        else:
            left += count + 1
            count = 0

    print(right, left)
    answer = min(right, left)
    return answer

def DFS(name, word, index, count):
    if name == word:
        return count

    right = 0
    left = 0

    # word = word[:index] + name[index] + word[index + 1:]
    # count += min(ord(name[index]) - ord("A"), 26 - (ord(name[index]) - ord("A")))

    right_word = word
    right_count = count
    for i in range(1, len(name)):
        if name[(index + i) % len(name)] != 'A':
            if name[index] != 'A':
                right = DFS(name, right_word, (index + i) % len(name), right_count + 1)

            right_word = word[:index] + name[index] + word[index + 1:]
            right_count += min(ord(name[index]) - ord("A"), 26 - (ord(name[index]) - ord("A"))) + 1
            continue

    left_word = word
    left_count = count
    for i in range(1, len(name)):
        if name[(index - i) % len(name)] != 'A':
            left_word = word[:index] + name[index] + word[index + 1:]
            left_count += min(ord(name[index]) - ord("A"), 26 - (ord(name[index]) - ord("A"))) + 1
            continue
        left = DFS(name, left_word, (index - i) % len(name), left_count + 1)
        break

    return min(right, left)

def solution(name):
    answer = 0
    word = "A" * len(name)

    answer = DFS(name, word, 0, 0)
    print(answer)

    return answer


# solution1("JEROEN")
solution("ABABAAAABA")
solution("B")
