import matrix


def list_rot90(data, times=1):
    rot_data = []
    for t in range(times):
        m = len(data)
        n = len(data[0])
        rev_data = data[:: -1]
        rot_data = [[rev_data[j][i] for j in range(m)] for i in range(n)]

        data = rot_data
    return rot_data


list = matrix.input_float_2list("Введите двумерны массив разделяя столбцы пробелами,\nа сторчки с помощью Enter. При завершении введите пустую строку.")

list = list_rot90(list)

for buffer in list:
    print(*buffer, sep=" ")
