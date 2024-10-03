
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(2, 'Hello')
print_params(2, 'Hello', False)

print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = [3, True, 'list_test']
value_dict = {'a': 5, 'b': False, 'c': 'dict_test'}
print_params(*value_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)


