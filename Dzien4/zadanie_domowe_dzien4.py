# Przeczytaj artykul:  https://www.geeksforgeeks.org/args-kwargs-python/

# 4. Napisz funkcję, która przyjmuje dowolną ilość parametrów - zaloz ze beda podawane liczbowe, funkcja ma wypisywac te parametry, uzywajac petli for in

def funkcja1(*argv):
    for element in argv:
        print(element)

funkcja1(1,2,3,4,5,18)


# 5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji

def funkcja2(*argv):
    for element in argv:
        print(element)
    suma=sum(argv)
    print(f"suma: {suma}")

funkcja2(1,2,3,4,5)


# 6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add) oraz mnozenie dwoch liczb (np o nazwie multiply),
# nastapnie wywolaj operację: multiply(add(2, 6), 2)

def add(*argv):
    suma=sum(argv)
    return suma

def multiply(suma,liczba):
    print(suma*liczba)

multiply(add(2,6),2)


# 7. Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami) oraz funkcje sortujaca liste slow,
# # nastepnie wywolaj sortowanie na slowach podanego przez uzytkownika zdania

zdanie=input("Wpisz zdanie do posortowania: ")

def rozbijanie_zdania(zdanie):
    wyrazy=zdanie.split()
    return wyrazy

def sortowanie(wyrazy):
    wyrazy.sort()
    print(wyrazy)

sortowanie(rozbijanie_zdania(zdanie))


# 8 (optional) Zaimportuj modul (plik) i uzyj funkcji z tego modulu
#  help(nazwa_pliku) - zadokumentuj troche kodu!

import split_sort

lista=split_sort.rozbijanie_zdania("halo halo hej czesc siemka czolem witam")

split_sort.sortowanie(lista)

print("\n\r\n\r HELP:\n\r")
help(split_sort)




#######################################################################################################################



# zadania dodatkowe


# Przeczytac https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36


# WSKAZÓWKI: nie musisz robić całego zadania na raz - rozbij sobie bardziej skomplikowane zadania na jak najmniejsze
# czesci, testuj i powiekszaj

# 1 stwórz kilka zmiennych różnych typów - int, float, boolean, string

int=35
flo=20.5
boo=True
str='Witaj'

# 2 za pomocą funkcji print() wypisz wartości powyższych zmiennych, podając ich typ (użyj funkcji type)
# pamiętaj o formatowaniu i znakach specjalnych, najlepiej aby pokazywać wartości wraz z typami zmiennych w nowej linii


print(f"Zmienna {int} - typ {type(int)}\r\nZmienna {flo} - typ {type(flo)}\r\nZmienna {boo} - typ {type(boo)}\r\nZmienna {str} - typ {type(str)}")


# 3. Wypisz zmienną typu float - dobrym przykladem bedzie liczba 1/17. z dokładnością do 4 miejsc po przecinku
# https://stackoverflow.com/questions/8885663/how-to-format-a-floating-number-to-fixed-width-in-python

float_number=1/17
print(f'{float_number:5.4f}')


# 4. Indeksowanie (slajd dzien 3 od strony 4)
# stwórz nową zmienną typu string oraz zmienną pomocniczą, do której przy pomocy indeksowania,
# przypiszesz odwrócony string pierwszej zmiennej (możesz przejrzeć slajd 4 z prezentacji dnia 3 i sprawdzic np w konsoli
# które indeksowanie odwraca)

string="dziendobry"
odwrocenie=string[::-1]
print(odwrocenie)


# 5. rozszerz zadanie 4 - sprawdź czy string jest palindromem

string="dziendobry"
odwrocenie=string[::-1]
print(odwrocenie)

if string==odwrocenie:
    print(f"Slowo {string} jest palindromem")
else:
    print(f"Slowo '{string}' nie jest palindromem")


# 6. przy pomocy funkcji input() rozszerz zadanie 5 tak aby uzytkownik wpisał słowo i program powiedział,
# czy wisane slowo jest palindromem

string=input("Wpisz slowo: ")
odwrocenie=string[::-1]
#print(odwrocenie)

if string==odwrocenie:
    print(f"Slowo '{string}' jest palindromem.")
else:
    print(f"Slowo '{string}' nie jest palindromem.")


# pętle oraz instruckje warunkowe

# 7. wykorzystaj funkcje input() i zagraj z uzytkownikiem programu w grę RPG
# Poinformuj użytkownika że stoi na rozdrozu - moze isc prosto, w lewo, lub w prawo
# aby pójść prosto - musi wpisać "straight", w lewo - "left", w prawo = "right"
# w zależności od wyboru ścieżki, poinformuj użytkownika kogo spotkał (dla Twojej wyobraźni sky is the limit)
# jeżeli użytkownik nie wpisał poprawnie kierunku - napisz że nie umie się grać...
# (do rozwiazania przyda się if elif else)

dir=input("Choose which direction to take: left, straight or right?")

if dir == "left":
    print("Oh, you really chose left direction? No way! It's really risky, the huge anaconda is somewhere there!")
elif dir == "straight":
    print("Straight way to hell! It's getting hot... Did you see this devil right there?")
elif dir == "right":
    print("It looks like a safe path. You just have to jump over the alligators.")
else:
    print("Oh man, you don't know how to play this easy game...")


# 8. rozszerz zadanie 7 w taki sposób, aby zachęcić użytkownika jeszcze raz do wyboru ścieżki, jeżeli nie wpisał komendy poprawnie
# (przyda się pętla while - mozesz zatrzymać skrypt ręcznie jeżeli w czasie wykonywania się zapętlił nie tak jak powinien)

dir=input("Choose which direction to take: left, straight or right?")

while (dir != "left" and dir != "straight" and dir != "right"):
    print("Oh man, you don't know how to play this easy game... Try again!")
    dir=input("Choose once again a direction:")
else:
    if dir == "left":
        print("Oh, you really chose left direction? No way! It's really risky, the huge anaconda is somewhere there!")
    elif dir == "straight":
        print("Straight way to hell! It's getting hot... Did you see this devil right there?")
    elif dir == "right":
        print("It looks like a safe path. You just have to jump over the alligators.")


# 9. Klasa range - przy użyciu pętli for in oraz użyciu range, wypisz tylko liczby podzielne przez 7 w zakresie 0-77
# wskazówka: przyda się warunek if oraz modulo %
# 4 % 2 == 0 -> true

for liczba in range(78):
    if liczba%7==0:
        print(liczba)


# 10. listy - [] wygeneruj 2 listy liczb o tych samych rozmiarach, ale różnych wartościach

lista1=[1,3,15,6,89]
lista2=[17,4,6,12,7]


# 11. stwórz nową listę, używając dwóch list z zadania 10. lista ma zawierać liczby z listy pierwszej podniesione
# przemnozone przez liczbę o tym samym indeksie z listy drugiej

lista3=[]
for x,y in zip(lista1,lista2):
    z=lista3.append(x*y)

print(lista3)