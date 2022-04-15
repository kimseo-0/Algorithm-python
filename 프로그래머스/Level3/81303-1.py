def solution(n, k, cmd):
    result = ['O' for _ in range(n)]
    index = [i for i in range(n)]
    delete = []

    for command in cmd:
        # print(k, index, result)
        if command == "C":
            result[index[k]] = 'X'
            delete.append(index.pop(k))

            if k == len(index):
                k -= 1

        elif command == "Z":
            restore_index = delete.pop()
            result[restore_index] = 'O'

            start = 0
            end = len(index) - 1
            insert_index = restore_index
            while start <= end:
                mid = (start + end) // 2

                if mid == len(index) - 1:
                    insert_index = mid + 1
                    break
                elif mid == 0:
                    insert_index = mid
                    break
                elif index[mid] < restore_index < index[mid + 1]:
                    insert_index = mid + 1
                    break
                elif index[mid - 1] < restore_index < index[mid]:
                    insert_index = mid
                    break

                if index[mid] > restore_index:
                    end = mid - 1
                else:
                    start = mid + 1

            index.insert(insert_index, restore_index)
            if k >= insert_index:
                k += 1

        else:
            action, num = command.split()
            if action == 'U':
                k -= int(num)
            elif action == 'D':
                k += int(num)

    # print(k, index, result)
    answer = ''.join(result)
    # print(answer)
    return answer


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
