# jako prace domową - przejrzyj zadania - examples z folderu Trainings - przykłady nie zaczynaja sie od numeru
# oraz rozwiaz zadania z folderu Trainings (pliki zaczynajace sie od numerow)


# Trainings/1_if_else_ex.py:

# oblicz czy rok jest przestępny
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = int(input("Podaj rok: "))

if (rok%4==0 and rok%100 != 0) or rok%400==0:
    print(f"Rok {rok} jest przestepny.")
else:
    print(f"Rok {rok} nie jest przestepny.")


# Trainings/2_if_else_ex.py

# podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if (bok_a < bok_b + bok_c) and (bok_b < bok_a + bok_c) and (bok_c < bok_a + bok_b):
    print(f"Uda sie narysowac trojkat o bokach: {bok_a}, {bok_b}, {bok_c}")
    if bok_a == bok_b == bok_c:
        print(f"Bedzie to trojkat rownoboczny")
    elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
        print(f"Bedzie to trojkat rownoramienny")
    else:
        print(f"Bedzie to trojkat roznoboczny")
else:
    print(f"Nie uda sie narysowac trojkatu o bokach: {bok_a}, {bok_b}, {bok_c}")


#Trainings/3_if_else_ex.py

 # zamiana temperatury
 #    wejscie: temperatura w C lub F, np: "35C" "100F"
 #    wyjście "Temperatura w {typ} to {xxx} stopni" - jezeli podano w F to wypisz w C i odwrotnie
 #    C = (F - 32) * (5/9)
 #    F = C * (9 / 5) + 32


skala=input("Podaj jednostke temperatury, jaka chcesz wprowadzic (C/F): ")
if skala.upper() == 'C':
    skala_docelowa='F'
    temp_c = int(input("Wprowadz temperature w stopniach Celsjusza: "))
    temp_f = temp_c * (9 / 5) + 32
    print(f"Temperatura w skali {skala_docelowa} to {int(temp_f)} stopni")
elif skala.upper() == 'F':
    skala_docelowa = 'C'
    temp_f = int(input("Wprowadz temperature w stopniach Fahrenheita: "))
    temp_c = (temp_f - 32) * (5 / 9)
    print(f"Temperatura w skali {skala_docelowa} to {int(temp_c)} stopni")
else:
    print(f"Wprowadzono bledna jednostke ({skala}). Sprobuj od nowa.")




#Trainings/4_for_loops_ex.py

# obl. ilość l. parzystych i nieparzystych w zakresie

zakres = range(23746)

parzyste = 0
nieparzyste = 0

for liczba in zakres:
    if liczba%2==0:
        parzyste+=1
    elif liczba%2!=0:
        nieparzyste+=1
#     tutaj nalezy napisac kod

print(f"Liczb parzystych: {parzyste}, liczb nieparzystych: {nieparzyste}")



#Trainings/5_for_loops.py

# policz samogloski i spolgloski
zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samogl = "aeiouyąęó"

for litera in zdanie:
    if litera in lista_samogl:
        samogloski+=1
    elif litera.isalpha():
        spolgloski+=1

print(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")





#Trainings/6_for_loops.py

# fizz buzz
# wypisac liczby od 1 do 100 (włącznie)
# zamiast l. podzielnych przez 3 wypisz Fizz
# zamiast liczb podzielnych przez 5 wypisz Buzz
# zamist liczb podzielnych przez 3 i 5 wypisz FizzBuzz

zakres = range(1, 101)

for liczba in zakres:
    if (liczba%3==0 and liczba%5==0):
        print('FizzBuzz')
    elif liczba%3==0:
        print('Fizz')
    elif liczba%5==0:
        print('Buzz')
    else:
        print(liczba)


#Trainings/7_while_loops.py - do dokonczenia

# program, ktory wypisze liczby (z zakresu 0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# propozycja uzycia petli while - ale kazde rozwiazanie jest dobre ;)

#
# # liczba = range(0, 101)
#
# liczba = 0
#
#
# # while liczba in range(0,101):
# if liczba == 0:
#     print(0)
#     liczba+=1
# elif liczba==1:
#     print(1)
#     suma=
# while liczba in range(0, 101):
#     print(f"liczba {liczba}")
#     poprzednia_liczba=liczba
#     print(f"poprzednia liczba {poprzednia_liczba}")
#     suma=liczba+poprzednia_liczba
#     print(f"suma {suma}")
#
#     # print(f"poprzednia liczba {poprzednia_liczba}")
#


#Trainings/8_func_1.py

# napisz funkcje obliczajaca pole kwadratu

def pole_kwadratu(bok_kwadratu):
    pole=bok_kwadratu**2
    return pole

print(pole_kwadratu(4))







# oraz:

# 1 stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# może być słownik miejskiego slangu ;)
# words_dict["kasiora"] = "Opis słowa kasiora"

slownik_slangu={'siano':'kasa','fura':'samochod','rejon':'okolica','szlugi':'papierosy'}
#print(slownik_slangu)


# 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# np kasiora - Opis slowa kasiora, w nowej linii nastepna para

slownik_slangu={'siano':'kasa','fura':'samochod','rejon':'okolica','szlugi':'papierosy'}

with open("slownik_slangu.txt", 'w') as plik_slang:
    for slowo, znaczenie in slownik_slangu.items():
        plik_slang.write(f'Slowo {slowo} znaczy {znaczenie} \n')


# 3 zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example

slownik_slangu={'siano':'kasa','fura':'samochod','rejon':'okolica','szlugi':'papierosy'}

import csv

with open('slownik_slangu_csv.csv', newline='', mode='w') as plik_slang_csv:
    writer = csv.writer(plik_slang_csv, delimiter="|")
    for linia in slownik_slangu.items():
        writer.writerow(linia)



# 4 zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# odczytaj plik i sprawdz czy poprawnie zapisano dane


slownik_slangu={'siano':'kasa','fura':'samochod','rejon':'okolica','szlugi':'papierosy'}

import pickle

# zapis:
with open("slang.pckl", 'wb') as plik_pickle:
    pickle.dump(slownik_slangu, plik_pickle)

#odczyt:
odczytany_plik = None

with open("slang.pckl", "rb") as plik_pickle:
    # musimy zwrócić uwagę na kodowanie, jeśli będą pojawiać się krzaczki
    odczytany_plik = pickle.load(plik_pickle)

print(odczytany_plik)



# 5 odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# (powiedz uzytkownikowi ile razy wystepuje)

slowo=input("Podaj slowo do wyszukania:")
slowo_lower=slowo.lower()

with open('article.txt', 'r+') as plik:
    plik_read=plik.read()
    plik_case=plik_read.lower().split()
    wystapienia=plik_case.count(slowo_lower)

print(f"Slowo {slowo} wystepuje w tekscie {wystapienia} razy.")




# 6 utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# na poczatku programu zaladuj slownik z pliku pickle
# (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany