import checker
import triangle


def input_float_list():
    is_string = False
    while True:
        list1 = list(input().split(" "))
        for number in range(len(list1)):
            if not checker.is_float(list1[number]):
                is_string = True

        if is_string:
            print("Ошибка! введён недопустимый тип данных")
            is_string = False
            continue
        break
    return [float(elem) for elem in list1]


def counting_of_occurrence(check_list: list, number: float):
    counter = 0
    for check_number in check_list:
        if number == check_number:
            counter += 1
    return counter


def create_new_list(first_list: list, second_list: list):
    new_list = list()
    for number in first_list:
        for i in range(counting_of_occurrence(second_list, number)):
            new_list.append(number)
    return new_list


file = open("./triangle.txt", 'r')
print(file.read())
s1 = triangle.Triangle(2, 0, 3, 2, 4, 0)
s2 = triangle.Triangle(1, 0, 3, 3, 5, 0)
s = [s2, s1]
f = sorted(s, key=triangle.Triangle.sort_key)
print(f)
