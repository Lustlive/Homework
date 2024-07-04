immutable_var = tuple([10, 'Привет, мир', True])
print(immutable_var)
#immutable_var[0][1] = 'Привет, вселенная'     !В кортежах хранятся неизменямые файлы!
mutable_list = ([1, 2, 3], 4, 5)
print(mutable_list)
mutable_list[0][2] = 30
print(mutable_list)

