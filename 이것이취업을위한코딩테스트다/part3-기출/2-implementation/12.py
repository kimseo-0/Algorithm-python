import sys
input = sys.stdin.readline


def check_build(answer):
    for frame in answer:
        [x, y, type] = frame
        if type == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ( [x - 1, y, 1] in answer and [x + 1, y, 1] in answer ):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        check = True
        [x, y, type, action] = frame
        if action == 1:  # 추가
            answer.append([x, y, type])
            if not check_build(answer):
                answer.remove([x, y, type])
        else:   # 삭제
            answer.remove([x, y, type])
            if not check_build(answer):
                answer.append([x, y, type])

    answer.sort()
    print(answer)
    return answer


solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
