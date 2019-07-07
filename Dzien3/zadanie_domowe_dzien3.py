# Odpalanie programu z command line:
#python <sciezka\program.py> np. python zadanie_domowe_dzien3.py

# Odpalanie programu z ARGUMENTAMI z command line:
#python <sciezka\program.py> np. python zadanie_domowe_dzien3.py "argument1" "argument2"



#1.	Napisz program analogiczny do powyższego (nie przejmuj się jeżeli nie rozumiesz pierwszej linii po prostu ją przepisz), gdzie podasz 3 liczby oraz wypiszesz sumę trzech podanych liczb

from sys import argv

program_name, first_arg, second_arg, third_arg = argv

wynik=int(first_arg)+int(second_arg)+int(third_arg)
print(f'Pierwszy argument: {first_arg}, Drugi argument: {second_arg}, Trzeci argument: {third_arg}, Suma argumentow: {wynik}')

# #alternatywa - drugi print pod spodem:
# wynik=int(first_arg)+int(second_arg)+int(third_arg)
# print(f'Suma argumentow: {wynik}')



#2.	Napisz program w którym podasz jako pierwszy argument zdanie, a drugi argument liczbę oznaczającą ile razy to zdanie powtórzyć.
# Wypisz tyle razy to zdanie – użyj pętli for in oraz klasy range

from sys import argv

program_name, zdanie, powtorzenie = argv

for index in range(int(powtorzenie)):
    print(zdanie)



#3.	Czytanie plików: Przeczytaj tekst: https://realpython.com/read-write-files-python/
# Oraz poćwicz odczytywanie danych z pliku – pamiętaj żeby plik był umieszczony najlepiej w tym samym miejscu co uruchamiany program, w przeciwnym wypadku podaj pełną ścieżkę do pliku

