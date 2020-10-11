some_list = list(input("введите через пробел любое количество элементов из которых будет сформирован список: ").split())
some_list_length = len(some_list)
c = some_list_length//2
i = 1
v = 0
while i <= c:
    some_list[v], some_list[v+1] = some_list[v+1], some_list[v]
    i += 1
    v += 2
print(some_list)