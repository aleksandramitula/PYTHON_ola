#1.	Napisz program analogiczny do powyższego (nie przejmuj się jeżeli nie rozumiesz pierwszej linii po prostu ją przepisz), gdzie podasz 3 liczby oraz wypiszesz sumę trzech podanych liczb

from sys import argv

program_name, first_arg, second_arg, third_arg = argv

wynik=int(first_arg)+int(second_arg)+int(third_arg)
print(f'Pierwszy argument: {first_arg}, Drugi argument: {second_arg}, Trzeci argument: {third_arg}, Suma argumentow: {wynik}')

# #alternatywa - drugi print pod spodem:
# wynik=int(first_arg)+int(second_arg)+int(third_arg)
# print(f'Suma argumentow: {wynik}')