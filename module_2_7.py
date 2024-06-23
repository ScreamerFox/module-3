def print_params(a = 1, b = 'строка', c = True):
        print(a, b, c)

values_list = [1.6, False, 'alahamora']
values_dict = {'a' : 56, 'b' : "stroka", 'c' : (5+6)}
values_list_2 = ["Игорь Потов", 89.64]


print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 1)
