def is_int(number):
    return __check(number, 'i')


def is_float(number):
    return __check(number, 'f')


def __check(number, format):
    try:
        if format == 'i':
            int(number)
        elif format == 'f':
            float(number)
        return True
    except ValueError:
        return False
