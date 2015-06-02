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


def vector_add(vector_1, vector_2):  # Works
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


def vector_sum(*args):  # Works
    args = list(args)
    # check_shape(args[0], args[1])
    for e, i in enumerate(args):
        if len(args[0]) != len(args[e]):
            raise ShapeException
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


def vector_mean(*args):  # Works
    answer = []
    list_to_work = vector_sum(*args)
    args = list(args)
    divide_by = len(args)
    for item in list_to_work:
        answer.append(item/divide_by)
    print(answer)
    return answer


def matrix_row(matrix_1, row_num):  # Works
    return matrix_1[row_num]


def matrix_col(matrix_1, col_num):  # Works
    answer = []
    init_list = [0 for x in range(len(matrix_1))]
    for n, num in enumerate(matrix_1):
        # print("Run")
        # print(init_list)
        for number, value in enumerate(num):
            # print(num[col_num])
            init_list[n] = num[col_num]
            # print(init_list)
    return init_list


def matrix_scalar_multiply(vector_1, z):  # Works
    final_answer = []
    init_list = [0 for x in range(len(vector_1[0]))]
    answer = []
    counter = 0
    for lists in vector_1:
        print(vector_1)
        if counter == 1:
            init_list = [0 for x in range(len(vector_1[0]))]
        final_answer.append(init_list)

        print(lists)
        counter = 1
        for num, item in enumerate(lists):
            print(item)
            init_list[num] = (item * z)
            print(init_list)
    return(final_answer)


def matrix_vector_multiply():  # Not Done
    answer = []
    for num in vector_1:
        for number in num:
            number = number * num
            answer.append(number)
        answer_2.append(answer)
        print(answer_2)
    return answer_2


def matrix_matrix_multiply(matrix_1, matrix_2):
    if matrix_col(matrix_1, 0) != matrix_row(matrix_2, 0):
        raise ShapeException
    """answer = []
    if matrix_col(matrix_1, 0) <= matrix_col(matrix_2, 0):
        run_matrix = matrix_2
        other_matrix = matrix_1
    else:
        run_matrix = matrix_1
        other_matrix = matrix_2
    for x,y in enumerate(run_matrix):
        answer.append(
            dot(matrix_col(run_matrix, x), matrix_row(other_matrix, x)))
    return answer"""
    if matrix_col(matrix_1, 0) <= matrix_col(matrix_2, 0):
        run_matrix = matrix_2
        other_matrix = matrix_1
    else:
        run_matrix = matrix_1
        other_matrix = matrix_2
    init_list = [[0 for row in range(
        len(other_matrix))] for col in range(len(run_matrix[0]))]
    print(init_list)
    for row in range(len(matrix_1)):
        for col in range(len(matrix_2[0])):
            for rows in range(len(matrix_2)):
                init_list[row][col] += matrix_1[row][rows] * matrix_2[rows][col]
    return(init_list)
