words = list(input("Введите слова через пробел: ").split())
i = 0
while i < len(words):
    print(words[i][0:10])
    i += 1