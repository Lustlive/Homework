def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# print_params(b = 25)
# print_params(c = [1,2,3])
# print_params()
# print()
#
# values_list = [17, 'String', True]
# values_dict = {3, 2, 1}
# print_params(*values_list)
# print_params(*values_dict)
# print()
#
#
# values_list_2 = ('Строка', False)
# print_params(*values_list_2, 42)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)