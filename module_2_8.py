def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[:1])
    if len(str_number) == 1:
        return int(str_number)
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits('203042')
print(result)
