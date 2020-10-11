test_var = 100
some_list = [12, "c", False, ["a", "b"], test_var, ("a", "b", "c"), ({"a", "b", "c", 10, 20}),
             {"key1": "val1", "key2": "val2"}, ]
some_list_length = len(some_list)
i = 0
while i < some_list_length:
    print(f"Тип {i} элемента списка {type(some_list[i])}")
    i += 1
