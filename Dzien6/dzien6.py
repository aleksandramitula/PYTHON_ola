# SLOWNIKI


# # lista ze slownikami:
#
# rekordy = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
# {"imie": "Anna", "nazwisko":"nowak", "wiek":23},
# {"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
# {"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]
#
# # nasza baza słownikowa jest uzupełniana elementami
# # tworzymy unikalny klucz - indeks z listy
#
# for indeks, rekord in enumerate(rekordy):
#     print(f"index:{indeks}, value:{rekord}")
#
# # stworzenie nowego slownika z indeksami i slownikami w srodku:
#
# nowy_slownik={}
# for indeks, rekord in enumerate(rekordy):
#     print(f"index:{indeks}, value:{rekord}")
#     nowy_slownik[indeks] = rekord
# print(nowy_slownik)




# simple_dict = {1:"jeden", 2:"dwa"}
#
# for key, value in simple_dict.items():
#     print(f"pod kluczem {key} jest wartosc {value}")
#
# simple_dics[1] = "trzy"


# # zalozyc slownik baza danych filmow: klucz = rok, value = nazwa filmu

# 1)
# movie_dict= {1996:"Pulp fiction", 1997:["Niekonczaca sie opowiesc","Glupi i glupszy","Cokolwiek"], 2017:"Manchaster by the sea"}
#
# for key, value in movie_dict.items():
#     print(f"W roku {key} ukazal sie film {value}")

#2)
movie_dict={}

movie_dict[2000]=["Animatrix","Matrix","Matrix II"]
movie_dict[2009]=["Transformers 2", "Transformers 3"]

for key, value in movie_dict.items():
    print(f"W roku {key} ukazal sie film {value}")

# dopisanie kolejnych filmow:
movie_dict[2000].append("Matrix III")


# po stworzeniu listy filmów w np. roku 2000 i 2009, wypisz ładnie ;) na konsoli rok, a następnie filmy w danym roku
# uzyj np wciecia, aby pokazac przynaleznosc danych filmow do roku


for key, value in movie_dict.items():
    print(key)
    for movie in value:
        print(f"\t{movie}")




# dictionaries plus lists
# napisz program odczytujacy plik - policz ilosc wystepujacych poszczegolnych slow
# Wskazowki:
# default dict values
# from collections import defaultdict
# set(
# list_dictionary = defaultdict(list)



