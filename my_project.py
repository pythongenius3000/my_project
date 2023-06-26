stroka = str(input('Введите строку без пробелов и в нижнем регистре: '))
stroka_opposite = stroka[::-1]
if stroka == stroka_opposite:
    print(True)
else:
    print(False)
