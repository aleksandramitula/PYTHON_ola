# # zakres zmiennych (global i nonlocal)
#
# # imie = 'Jola'
# # def zmien_imie():
# #     imie = 'Teresa'
# #
# # print(imie)
# # zmien_imie()
# # print(imie)
# # zawsze wyprintuje Jola, bo to z funkcji istnialo tylko przez chwile w momencie trwania tej funkcji.
#
#
# # sprobowac to samo zrobic z nadaniem argumentu oraz z lista ??
#
#
#
#
# # Dokumentowanie kodu - opis funkcji:
# # wpisujemy """ i klikamy enter - umieszcza sie automatycznie miejsca do opisu argumentow
#
# def dodawanie(x,y):
#     """
#     Return sum of two arguments.
#     :param x: first argument
#     :param y: second argument
#     :return: sum
#     """
#     suma=x+y
#     return suma
#
# # Aby zobaczyc dokumentacje tej funkcji wpisujemy:
#
# print(dodawanie.__doc__)
#
#
#
# # Dopisywanie kolejnych imion do listy:

#
# def dodaj_imie(imie, imiona=[]):
#     imiona.append(imie)
#     return imiona
#
# print(dodaj_imie("halo"))
# print(dodaj_imie("elo"))
# print(dodaj_imie("hej"))
# print(dodaj_imie("czesc"))


#######################################################################################################################


# ZADANIA:



# # 1. napisz funkcję sumujący wszystkie elementy w liscie

# lista=[1,2,3,4]
# def suma_listy(lista):
#     suma=sum(lista)
#     return suma
#
# print(suma_listy(lista))


# # 2. znajdz najwiekszy / najmniejszy element w liscie - napisz dwie funkcje
# # dwa sposoby - najpierw ręcznie, następnie sprytnie

# 1) Uzycie MIN i MAX

# lista=[1,2,3,4,5]
# def max_min_list(lista):
#     max_list=max(lista)
#     min_list=min(lista)
#     return max_list, min_list
#     # print(f"Max: {max_list}")
#     # print(f"Min: {min_list}")
#
# print(f"Max, min: {(max_min_list(lista))}")


# 2) Uzycie SORT

# lista=[1,2,3,4,5]
# def max_min_list_sorted(list):
#     list.sort()
#     max_list=list[-1]
#     min_list=list[0]
#     return max_list, min_list
#     # print(f"Max: {max_list}")
#     # print(f"Min: {min_list}")
#
# print(f"Max, min: {(max_min_list_sorted(lista))}")
# # lub
# # print(f"Max, min: {(max_min_list_sorted([1,2,3,4,5]))}")





# # 3. funkcja ktory zmieni zdanie w liste wyrazow
# zdanie = "Ala ma kota, kot ma Ale"

# sentence="Ala ma kota, kot ma Ale"
# def sentence_to_list(sentence):
#     list=sentence.split()
#     return list
#
# print(sentence_to_list(sentence))



# # 4. napisz funckję przyjmujaca liste stringow,
# # a zwracakaca liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# # ['abc', 'xyz', 'aba', '1221'] - odp = 2


# 1) opcja ze stworzeniem listy:

# list_string=['abc','xyz','aba','1221']
#
# def find_string(list_string):
#     list = []
#     for slowo in list_string:
#         leng=len(slowo)
#         start=slowo[0]
#         end=slowo[-1]
#         if leng>=2 and start==end:
#             list.append(slowo)
#     return len(list)
#
# print(find_string(list_string))

# 2) opcja z counterem:

# list_string=['abc','xyz','aba','1221']
#
# def find_string(list_string):
#     counter = 0
#     for slowo in list_string:
#         if len(slowo)>=2 and slowo[0]==slowo[-1]:
#             counter=counter+1
#     return counter
#
# print(find_string(list_string))



# # 5. program znajdujacy wartosci, ktre wystepuja tylko raz
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]

# 1) counter:
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
# def wartosci_wystepujace_raz(lista_a):
#     for element in lista_a:
#         count=lista_a.count(element)
#         if count==1:
#             print(element)
#
# wartosci_wystepujace_raz(lista_a)

# 2) lista - mozna wypisac do listy, aby nie bylo printa w srodku funkcji:

# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
# def wartosci_wystepujace_raz(lista_a):
#     list_of_valid_numbers=[]
#     for element in lista_a:
#         if lista_a.count(element)==1:
#             list_of_valid_numbers.append(element)
#     return list_of_valid_numbers
#
# print(wartosci_wystepujace_raz(lista_a))



# # 6. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
# # podpowiedz - del lub pop()
# lista_b = [10,20,30,20,10,50,60,40,80,50,40]


# lista_b = [10,20,30,20,10,50,60,40,80,50,40]
# def usuwanie_duplikatow(lista_b):
#     for element in lista_b:
#         count=lista_b.count(element)
#         if count!=1:
#             lista_b.remove(element)
#     return lista_b
#
# print(usuwanie_duplikatow(lista_b))


#
# # 7. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# # jesli tak wypisuje True

# lista_1=[1,2,3,4,5,6,7]
# lista_2=[8,9,1]
#
#
# def listy_wspolny_element(lista_1, lista_2):
#     for value_1 in lista_1:
#         if value_1 in lista_2:
#             return True
#
#
# print(listy_wspolny_element(lista_1, lista_2))


#
# # 8. stworz macierz (4 x 5), ktorej wszystkie komorki wypelnione sa znakiem *

# def generate_matrix():
#     result=[]
#     for i in range(4):
#         col=[]
#         for j in range(5):
#             col.append('*')
#         result.append(col)
#     return result
# print(generate_matrix())

# 9. wybierz losowo element z listy
# wskazowka - import random

# import random
# list=["hej","jeden","dwa","trzy","cztery"]
# def chose_random_from_list(list):
#     result=random.choice(list)
#     return result
#
# print(chose_random_from_list(list))


# 9. oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# druga - moze jest jakis modul gotowy???
# my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]


my_list = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]
def count_occ(my_list):
    result=[]
    for element in my_list:
        count=my_list.count(element)

        # small_list=[element,count]
        # result.append(small_list)
    unique=set(my_list)
    return result

print(count_occ(my_list))