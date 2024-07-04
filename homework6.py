my_dict = {'Дима': 1971, 'Егор': 2002, 'Аня': 1989}
print(my_dict)
print(my_dict.keys())
print(my_dict.get('Егор'))
print(my_dict.get('Настя'))
my_dict.update({'Виктор': 2000 })
del my_dict['Аня']
print(my_dict)

my_set = {1, 2, 1, 2, 2, 3, 4, 4, 5, 'Привет', (1, 2, 3)}
print(my_set)
my_set.update({8, 9})
print(my_set)
my_set.discard(2)
print(my_set)


