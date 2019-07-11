## PLIKI


# # 1) czytanie calego pliku txt
# sciezka = "tekst1.txt"
#
# # otwieramy plik w trybie tekstowym, tylko do odczytu
# plik = open(sciezka, 'r')
#
# # read() czyta zawartość, od miejsca w któym jest kursor
# # aż do kocńa pliku
# tresc = plik.read()
# print(tresc)
#
# # pamiętać o zamykaniu pliku
# plik.close()



# # 2)

# sciezka = "tekst1.txt"
#
# # klauzula with ułatwia pracę z plikami
# # nie musimy pamiętać o zamykaniu pliku
# with open(sciezka) as plik:
#     # readline odczytuje jedną linijkę
#     # po odczytaniu, kursor ustawia się na początku
#     # kolejnej linijki (o ile jest jeszcze)
#     linijka = plik.readline()
#     # tell mówi nam w którym miejscu w pliku znjaduje
#     # się kursor
#     pozycja = plik.tell()
#     print(f"Kursor znajduje się w pozycji nr {pozycja}")
#
#     # print(linijka, end='')
#     # print("Kolejna linijka")
#     # print(plik.read())
#
#     # seek przenosi kursor we wskazaną pozycję
#     plik.seek(3)
#     print(plik.read())



# # 3) zaczytywanie linijek z pliku jako LIST


# sciezka = "tekst1.txt"
#
# with open(sciezka) as plik:
#     print(plik.tell())
#
#     # readlines odczytuje zawartość od kursora do końca
#     # poszczególne linijki będą elementami listy
#     # uwaga odczytywanie pliku powoduje odczytanie
#     # znaków niedrukowalnych - takich jak taby i znaki nowej linii
#     linijki = plik.readlines()
#
#     print(linijki)
#
#     for linijka in linijki:
#         # print(linijka)
#         print(linijka, end='')


# # 4) dopisywanie na koniec tekstu (append)

# sciezka = "tekst1.txt"
#
# with open(sciezka, 'a') as plik:
#     print(plik.tell())
#
#     plik.write("\nMoja kolejna linijka")




## 5) """ to jest wprowadzenie multiline - wszystkie znaki specjalne, nowe linie itp tez sa zapisywane """
## wprowadzanie - podmienianie tekstu od 0 indeksu, od poczatku pliku

# sciezka = "tekst1.txt"
#
# tekst = """blablblalbst. To
# jest kolejna linijka tekstu,
#         a to dandakp."""
#
# with open(sciezka, 'r+') as plik:
#     print(plik.tell())
#     plik.write(tekst)
#     #plik.seek(0) # musimy ustawic kursor na miejscu 0 (na poczatku pliku),
#     # poniewaz read czyta nam od polozenia kursora (czytli dopisal nowy tekst i za tym miejscem znajduje sie kursor
#     print(plik.read())



#
# ## 6)
# sciezka = "tekst1.txt"
#
# tekst = "Ten tekst jest zawsze w nowej linii"
#
# # ten sposób umożliwia nam dopisywanie treści zawsze w nowej linijce
#
# with open(sciezka, "r+") as plik:
#     # print(plik.tell())
#     # idziemy kursorem na koniec pliku
#     plik.read()
#
#     # bierzemy numer ostatniej pozycji
#     # i cofamy kursor na przedostatnią pozycję
#     pozycja = plik.tell()
#     plik.seek(pozycja - 1)
#
#     # odczytujemy ostatni znak
#     ostatni_znak = plik.read()
#     print(ostatni_znak)
#
#     # teraz wiemy, że jeśli ostatni znak nie jest znakiem nowej linii
#     # to w pliku nie ma na końcu pustego wiersza
#     if ostatni_znak != '\n':
#         plik.write('\n' + tekst + '\n')
#     # a tu był znak nowej linii, czyli plik miał pusty wiersz
#     else:
#         plik.write(tekst + '\n')



## Stworz plik z filmami (filmy), aby kazdy film byl w nowej linii:

list_of_movies = ["obcy 3","terminator","dawno temu w trawie"]


with open('filmy.txt', 'w') as plik:
    for film in list_of_movies:
        plik.write(film+'\n')

# ## alternatywa:
# with open('filmy.txt', 'w') as plik:
#     plik.writelines(list_of_movies) # ale wypisze nam liste w jednej linijce

# # jezeli chcemy w konsoli podczytac ten plik, to musimy zmienic tryb otwarcia pliku na 'r+'
#     plik.seek(0)
#     print(plik.read())


## Zapisz plik tak samo, jak zrobilismy to w zadaniu ze slownikami:

# movie_dict={}
#
# movie_dict[2000]=["Animatrix","Matrix","Matrix II"]
# movie_dict[2009]=["Transformers 2", "Transformers 3"]
#
#
#
# with open('filmy_slownik.txt', 'w') as plik:
#     for key, value in movie_dict.items():
#         plik.write(str(key)+'\n')
#         for movie in value:
#             plik.write('\t'+movie+'\n')




# dictionaries plus lists
# napisz program odczytujacy plik - policz ilosc wystepujacych poszczegolnych slow
# Wskazowki:
# default dict values
# from collections import defaultdict
# set(
# list_dictionary = defaultdict(list)

# wypisz 10 najczęsciej i 10 najrzadziej wystepujacych slow

# simple_dict = {1: "jeden", 2: "dwa"}
#
# for key, value in simple_dict.items():
#     print(f"pod kluczem {key} jest wartosc: {value}")
#
# simple_dict[1] = "trzy"
#
# for key, value in simple_dict.items():
#     print(f"pod kluczem {key} jest wartosc: {value}")

# dictionaries plus lists
# napisz program odczytujacy plik - policz ilosc wystepujacych poszczegolnych slow


# from collections import defaultdict
# slownik={}
#
# with open('article.txt', 'r') as plik:
#     caly_text=plik.read()
#     slownik={caly_text}
#     #print(caly_text)
#     #defaultdict(caly_plik)
#     # to_words=caly_text.split
#     print(slownik)
#     # unique=set(list_to_words)
#     # print(unique)







from collections import defaultdict
#lista=[]

with open('article.txt', 'r') as plik:
    list_dictionary = defaultdict(list)
    caly_text=plik.readline()
    for linia in caly_text:
        splitted=caly_text.split
        text_set=set(splitted)
    #lista=[caly_text]
    dd=defaultdict(int)

    for k in caly_text:
        dd[k] +=1
    print(sorted(dd.items()))



#     slownik={caly_text}
#     #print(caly_text)
#     #defaultdict(caly_plik)
#     # to_words=caly_text.split
#     print(slownik)
#     # unique=set(list_to_words)
#     # print(unique)
#
#
# >>> s = 'mississippi'
# >>> d = defaultdict(int)
# >>> for k in s:
# ...     d[k] += 1
# ...
# >>> sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]