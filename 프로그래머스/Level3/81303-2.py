# 표 편집

class Node:
    def __init__(self, index):
        self.index = index
        self.up = index - 1
        self.down = index + 1

def solution(n, k, cmd):
    result = ['O' for _ in range(n)]
    table = [Node(i) for i in range(n)]
    table[0].up = None
    table[n - 1].down = None

    delete = []
    for command in cmd:
        print(k, result, delete)
        for t in table:
            print((t.up, t.down), end=",")
        print()
        if command == "C":
            result[k] = 'X'
            delete.append(k)

            if table[k].up is not None:
                table[table[k].up].down = table[k].down
            if table[k].down is not None:
                table[table[k].down].up = table[k].up
                k = table[k].down
            else:
                k = table[k].up

        elif command == "Z":
            restore_index = delete.pop()
            result[restore_index] = 'O'

            if table[restore_index].up is not None:
                table[table[restore_index].up].down = table[restore_index].index
            if table[restore_index].down is not None:
                table[table[restore_index].down].up = table[restore_index].index

        else:
            action, num = command.split()
            if action == 'U':
                for i in range(int(num)):
                    k = table[k].up
            elif action == 'D':
                for i in range(int(num)):
                    k = table[k].down
    print(k, result)

    answer = ''.join(result)
    print(answer)
    return answer


# solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "Z", "Z"])
solution(8, 2, ["C", "D 2", "C", "U 2", "C", "Z", "Z", "Z"])
# solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
