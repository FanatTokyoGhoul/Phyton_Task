import checker


def input_float_list(text):
    is_string = False
    while True:
        list1 = list(input(text).split(" "))
        for number in range(len(list1)):
            if not checker.is_float(list1[number]):
                is_string = True

        if is_string:
            print("Ошибка! введён недопустимый тип данных")
            is_string = False
            continue
        break
    return [float(elem) for elem in list1]


def input_float_2list(text):
    matrix = list()

    is_string = False

    print(text)
    while True:
        str = input()

        if str == "":
            break

        list1 = list(str.split(" "))

        for number in range(len(list1)):
            if not checker.is_float(list1[number]):
                is_string = True

        if is_string:
            print("Ошибка! введён недопустимый тип данных")
            is_string = False
            continue

        matrix.append([float(elem) for elem in list1])

    return matrix
