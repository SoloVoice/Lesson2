some_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
user_input = int(input("Существует список с элементами от 9 до 1. Введите число для размещения в списке: "))
if some_list.count(user_input) > 0:
    some_list.reverse()
    some_list.insert(some_list.index(user_input), user_input)
    some_list.reverse()
else:
    some_list.append(user_input)
print(some_list)