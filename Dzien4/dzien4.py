# # 1. Przypisanie nowej wartosci do elementu listy:
#
# # LISTA - REFERENCJA
#
# old_list = [1,2,3]
# new_list = old_list #przypisanie (w pamieci), ze nowa lista to jest to samo, co stara lista = referencja
#
# old_list[0] = 4
# print(old_list)
# print(new_list)
#
# # SAMA WARTOSC - typ prosty/wartosciowy - NIE REFERENCJA
#
# old_num = 4
# new_num = old_num
# old_num = 6
#
# print(old_num)
# print(new_num)
#
#
# # 2. Zachowanie obu list:
# old_list = [1,2,3]
#
# # skopiowanie starej listy do nowej
# new_list = old_list.copy()
#
# # stworzenie nowej listy ze zmiennej stara lista
# new_list = list(old_list)
#
# #
# new_list = old_list[:]
#
# # dopiero potem wystepuje zamiana wartosci starej listy, dlatego nie zmieniaja sie obie listy:
# old_list[0] = 4
#
# print(old_list)
# print(new_list)



# # 3. Zrobic zmienna liste, wygenerowac za pomoca klasy range 0-9 i skopiowac do nowej listy i przetworzyc druga, aby zawierala kwadraty tych liczb
#
# # Pierwszy sposob - tworzymy nowa liste jako pusta, i do niej dopisujemy wartosci poprzez append:
# old = list(range(10))
# new = []
#
# for wartosc in old:
#     new.append(wartosc**2)
#
# print(old)
# print(new)
#
#
# Drugi sposob - nowa lista jest kopia starej listy i podmieniana jest kazda wartosc
# old = list(range(10))
# new = list(old)
#
# new = [wartosc**2 for wartosc in new]
#
# print(old)
# print(new)

# # przydaje sie tez do stringow:
# old_words = ["iT's","eEdDs","PYYThon"]
# new_words = [word.upper() for word in old_words]
#
# print(old_words)
# print(new_words)

#
# # Trzeci sposob - nowa lista jest kopia starej listy. wyciagany jest indeks i wartosc z listy i podmieniana jest kazda wartosc dla danego indexu
#
# old = list(range(10))
# new = old[:]
# # old and new = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for indeks, wartosc in enumerate(old):
#     #print(f"{indeks} : {wartosc} ")
#     new[indeks] = wartosc ** 2
#
# print(old)
# print(new)



# 4. Stworzyc dwie listy o takiej samej dlugosci, ale o roznych liczbach. Stworzyc trzecia liste, ktora doda obie wartosci z list poprzednich na tym samym indeksie

list_one=list(range(1,9))
list_two=list(range(10,19))
list_tree=[]

for element_a, element_b in zip(list_one, list_two):
    element_c=element_a+element_b
    list_tree.append(element_c)

print(list_one)
print(list_two)
print(list_tree)

