stroka = str(input('Введите строку без пробелов и в нижнем регистре пожалуйста: '))
for n in stroka.split():
    #stroka_opposite = stroka[::-1], end=' '
    stroka_opposite = stroka[::-1]
#print(stroka_opposite)
if stroka == stroka_opposite:
    print(True)
else:
    print(False)
