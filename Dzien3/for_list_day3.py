#repeatHowManyTimes = int(input("Please tell me how many times to repeat."))

#range(repeatHowManyTimes) - wygenerowanie listy
#index - cokolwiek mozna zamiast tego wpisac, taka jest konstrukcja kodu, ze cokolwiek tutaj sie wpisze, to on bedzie bral elementy z listy.

# for index in range(repeatHowManyTimes):
#     print("hejo")


# 0 przypisz do zmiennej o odpowiedniej nazwie nazwy miesiaca (January, February) - mozna uzyc skrotow Jan, Feb itd...
# wypisz nazwy miesiaca funkcja print()
# nazwy miesiaca musza byc oddzielone enterem (znak specjalny \n)


# miesiace=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#
# #1)
# for element in miesiace:
#     print(element)
#
# #2)
# for element,wartosc in enumerate(miesiace):
#     print(str(element)+" "+str(wartosc))



# # 1 wypisz co druga literę z napisu - uzyj petli for: text = "Python is a fantastic snake"

#1)  #moje rozwiazanie, zle...
# text = "Python is a fantastic snake"
# for index in text:
#     print(text[::2])

#2)
# text = "Python is a fantastic snake"
# for index in text[::2]:
#     print(index)

#3)
# text = "Python is a fantastic snake"
# characters=len(text)
# #print(characters)
# list_of_indexes = range(0,characters,2)
#
# for index in list_of_indexes:
#     #print(index)
#     print(text[index],end='') #domyslnie konczy printowanie enterem, a teraz nadajemy mu, zeby konczyl pustym stringiem (niczym)



# # 1.1 skrot - przeczytaj https://docs.python.org/release/2.3.5/whatsnew/section-slices.html i wypisz co druga litere, tym razem w krotszy sposob

# text = "Python is a fantastic snake"
#
# wynik=text[::2]
# print(wynik)



# # 1.2 wypisz teraz co trzecią literę :wink:

# text = "Python is a fantastic snake"
#
# wynik=text[::3]
# print(wynik)


# # 2 wyszukaj w dokumentacji jak rozbić powyższy tekst na listę słów a nastepnie wydrukuj ta liste (for slowo in lista)

# text = "Python is a fantastic snake"
#
# lista=text.split()
# #print(lista)
# for slowo in lista:
#     #print(slowo)
#     #print(slowo,end=' ')



# # 3 zmien program z punktu drugiego tak, aby uzytkownik sam wpisal jakis tekst, ktory program mu rozbije na liste slow

text = input('Wpisz zdanie: ')

lista=text.split()
#print(lista)
for slowo in lista:
    print(slowo)
    #print(text[slowo],end=' ') #nie dziala!