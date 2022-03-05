import sys
from copy import deepcopy

input = sys.stdin.readline

def min_calculation(index, operation, calculation_result, operation_count):
    if index == N:
        return calculation_result

    if operation == 0:
        calculation_result += num_list[index]
        operation_count[0] -= 1
    elif operation == 1:
        calculation_result -= num_list[index]
        operation_count[1] -= 1
    elif operation == 2:
        calculation_result *= num_list[index]
        operation_count[2] -= 1
    elif operation == 3:
        if calculation_result < 0:
            calculation_result = -1 * (abs(calculation_result) // num_list[index])
        else:
            calculation_result //= num_list[index]
        operation_count[3] -= 1

    if sum(operation_count) == 0:
        return calculation_result

    result = []
    for i in range(4):
        # 언제 값들을 복사할지! 주의하자!
        new_index = index + 1
        new_calculation_result = calculation_result
        new_operation_count = deepcopy(operation_count)
        # print(new_index, new_calculation_result, new_operation_count)
        if new_operation_count[i] != 0:
            result.append(min_calculation(new_index, i, new_calculation_result, new_operation_count))

    # print(result)
    return min(result)


def max_calculation(index, operation, calculation_result, operation_count):
    if index == N:
        return calculation_result

    if operation == 0:
        calculation_result += num_list[index]
        operation_count[0] -= 1
    elif operation == 1:
        calculation_result -= num_list[index]
        operation_count[1] -= 1
    elif operation == 2:
        calculation_result *= num_list[index]
        operation_count[2] -= 1
    elif operation == 3:
        if calculation_result < 0:
            calculation_result = -1 * (abs(calculation_result) // num_list[index])
        else:
            calculation_result //= num_list[index]
        operation_count[3] -= 1

    if sum(operation_count) == 0:
        return calculation_result

    result = []
    for i in range(4):
        new_index = index + 1
        new_calculation_result = calculation_result
        new_operation_count = deepcopy(operation_count)
        # print(new_index, new_calculation_result, new_operation_count)
        if new_operation_count[i] != 0:
            result.append(max_calculation(new_index, i, new_calculation_result, new_operation_count))

    # print(result)
    return max(result)


N = int(input())
num_list = list(map(int, input().split()))
operation_list = list(map(int, input().split()))

answer = num_list[0]

print(max_calculation(0, -1, answer, operation_list))
print(min_calculation(0, -1, answer, operation_list))


