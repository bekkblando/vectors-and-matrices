import math


class ShapeException(Exception):
    pass


def dot(vector_1, vector_2):  # Works
    check_shape(vector_1, vector_2)
    answer = 0
    for num, value in enumerate(vector_1):
        answer = answer + (vector_1[num] * vector_2[num])
    return answer


def magnitude(vector_1):  # Works
    answer = 0
    for num in vector_1:
        answer = answer + (num * num)
    answer = math.sqrt(answer)
    return answer


def check_shape(matrix_1, matrix_2):
    if shape(matrix_1) != shape(matrix_2):
        raise ShapeException


def shape(matrix_1):
    try:
        len(matrix_1[0])
        return (len(matrix_1), len(matrix_1[0]))
    except:
        pass
    return (len(matrix_1), )


def vector_add(vector_1, vector_2):
    check_shape(vector_1, vector_2)
    answer = []
    for num, value in enumerate(vector_1):
        answer.append(vector_1[num] + vector_2[num])
    return answer


def vector_sub(vector_1, vector_2):  # Works
    check_shape(vector_1, vector_2)
    answer = []
    for num, value in enumerate(vector_1):
        answer.append(vector_1[num] - vector_2[num])
    return answer


def vector_sum(*args):
    args = list(args)
    # check_shape(args[0], args[1])
    init_list = [0 for x in range(len(args[0]))]
    math_work = 0
    for item in args:
        for num, value in enumerate(item):
            init_list[num] += item[num]
    return init_list


def vector_multiply(vector_1, z):  # Works
    answer = []
    for e, i in enumerate(vector_1):
        math_ans = vector_1[e] * z
        answer.append(math_ans)
    return answer


def vector_mean(*args):
    answer = []
    list_to_work = vector_sum(args)
    for num, item in list_to_work:
        answer.append(list_to_work[num]/2)
    return answer


def matrix_row(matrix_1, row_num):
    return matrix_1[row_num]


def matrix_col(matrix_1, col_num):
    answer = []
    for num in matrix_1:
        for number in value:
            answer.append(value[col_num])
    return answer


def matrix_scalar_multiply(vector_1, z):
    answer = []
    answer_2 = []
    for num in vector_1:
        for number, value in enumerate(num):
            num[number] = value * num
    return vector_1


def matrix_vector_multiply():
    answer = []
    for num in vector_1:
        for number in num:
            number = number * num
            answer.append(number)
        answer_2.append(answer)
        print(answer_2)
    return answer_2

C = [[1, 2],
     [2, 1],
     [1, 2]]
print(matrix_scalar_multiply(C, 3))


def matrix_matrix_multiply():
    pass
