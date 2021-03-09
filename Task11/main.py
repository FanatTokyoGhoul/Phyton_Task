import checker


def input_int_list():
    is_string = False
    while True:
        list1 = list(input("Введите список через пробел.\n").split(" "))
        for number in range(len(list1)):
            if not checker.is_int(list1[number]) or len(list1) < 2:
                is_string = True

        if is_string:
            print("Ошибка! введён недопустимый тип данных")
            is_string = False
            continue
        break
    return [int(elem) for elem in list1]


def progress(list: list):
    min_element = min(list)
    max_element = max(list)
    n = len(list)
    d = (max_element - min_element) / (n - 1)

    if int(d) != float(d):
        return False

    buff = min_element

    for number in range(n):
        if buff in list:
            buff += d
        else:
            return False

    return True


int_list = input_int_list()

if progress(int_list):
    int_list.sort()
    print(*int_list, sep=", ")
    print(f"d = {int_list[1] - int_list[0]}")
else:
    print("Это не арифмитиеская прогрессия!")
