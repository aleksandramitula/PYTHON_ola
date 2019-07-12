# # jako prace domową - przejrzyj zadania - examples z folderu Trainings - przykłady nie zaczynaja sie od numeru
# # oraz rozwiaz zadania z folderu Trainings (pliki zaczynajace sie od numerow)
#

# # Trainings/1_if_else_ex.py:
#
# # oblicz czy rok jest przestępny
# # podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400
#
# rok = int(input("Podaj rok: "))
#
# if (rok%4==0 and rok%100 != 0) or rok%400==0:
#     print(f"Rok {rok} jest przestepny.")
# else:
#     print(f"Rok {rok} nie jest przestepny.")


# # Trainings/2_if_else_ex.py

# # podane 3 boki trojkata, okresl
# #     - czy uda sie narysowac trojkata
# #       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
# #     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny
#
# bok_a = int(input("Podaj bok a: "))
# bok_b = int(input("Podaj bok b: "))
# bok_c = int(input("Podaj bok c: "))
#
# if (bok_a < bok_b + bok_c) and (bok_b < bok_a + bok_c) and (bok_c < bok_a + bok_b):
#     print(f"Uda sie narysowac trojkat o bokach: {bok_a}, {bok_b}, {bok_c}")
#     if bok_a == bok_b == bok_c:
#         print(f"Bedzie to trojkat rownoboczny")
#     elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
#         print(f"Bedzie to trojkat rownoramienny")
#     else:
#         print(f"Bedzie to trojkat roznoboczny")
# else:
#     print(f"Nie uda sie narysowac trojkatu o bokach: {bok_a}, {bok_b}, {bok_c}")


##Trainings/3_if_else_ex.py

#  zamiana temperatury
#     wejscie: temperatura w C lub F, np: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni" - jezeli podano w F to wypisz w C i odwrotnie
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32


# skala=input("Podaj jednostke temperatury, jaka chcesz wprowadzic (C/F): ")
# if skala.upper() == 'C':
#     skala_docelowa='F'
#     temp_c = int(input("Wprowadz temperature w stopniach Celsjusza: "))
#     temp_f = temp_c * (9 / 5) + 32
#     print(f"Temperatura w skali {skala_docelowa} to {int(temp_f)} stopni")
# elif skala.upper() == 'F':
#     skala_docelowa = 'C'
#     temp_f = int(input("Wprowadz temperature w stopniach Fahrenheita: "))
#     temp_c = (temp_f - 32) * (5 / 9)
#     print(f"Temperatura w skali {skala_docelowa} to {int(temp_c)} stopni")
# else:
#     print(f"Wprowadzono bledna jednostke ({skala}). Sprobuj od nowa.")











# # oraz:
#
# # 1 stwórz słownik, którego kluczem będą słowa, natomiast wartością znaczenie tych słów
# # może być słownik miejskiego slangu ;)
#
# # words_dict["kasiora"] = "Opis słowa kasiora"
#
# # 2 zapisz prosta zawartosc slownika miejskiego slangu do pliku, w kazdej linii klucz - wartosc
# # np kasiora - Opis slowa kasiora, w nowej linii nastepna para
#
# # 3 zapisz slownik slangu miejskiego do pliku csv, gdzie klucz (slowo) i wartosc (wyjasnienie slowa)
# # beda oddzielone pionową linią pipe (|) - przyklad zapisu pliku csv w Day6\exercises\cs_example
#
# # 4 zapisz slownik slangu miejskiego jako pickle - przyklad w Day6\exercises\pickle_1.py
# # odczytaj plik i sprawdz czy poprawnie zapisano dane
#
# # 5 odczytaj plik article.txt w calosci - plik umieszczony w Day5\exercises\article.txt
# # pozwol uzytkownikowi na podanie slowa i policz ile razy dane slowo wystepuje w artykule
# # (powiedz uzytkownikowi ile razy wystepuje)
#
# # 6 utwórz program, w ktorym uzytkownik bedzie mogl powiekszac baze slow slangu miejskiego
# # na poczatku programu zaladuj slownik z pliku pickle
# # (sprawdz czy plik istnieje, albo po wykonaniu zadania 4 uzyj istniejacego pliku)
# # napisz program tak, aby uzytkownik mogl dodawac slowa i ich wyjasnienie, dopoki nie zechce wyjsc z programu
# # (moze byc krotkie pytanie czy chcesz dodac slowo do slownika? TAK/NIE)
# # na koncu programu zapisz slownik ponownie do pliku pickle, aby zapisac zmiany