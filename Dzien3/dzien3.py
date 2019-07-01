# temperature = input("Podaj temperature: ")
# #DUZYMI LITERAMI piszemy stala, nie zmienna. To sa te wartosci, ktorych nie chcemy zmieniac w srodku w kodzie, ale mozna zmienic na poczatku:
# HOT_TEMPERATURE=30
# WARM_TEMPERATURE=25
# NOT_COLD_NOT_WARM_TEMPERATURE=20
#
# if temperature >=HOT_TEMPERATURE:
#     print("it's hot")
# elif temperature >=WARM_TEMPERATURE:
#     print("it's warm")
# elif temperature >=NOT_COLD_NOT_WARM_TEMPERATURE:
#     print("it's not warm or cold")
# else:
#     print("it's cold")



# napisz program
#jezeli a - napisz "zaczyna sie na 1 litere alfabetu", jezeli z - zaczyna sie na ostatnia, jezeli inaczej -  zaczyna sie na inna litere alfabbetu


slowo=input("Podaj slowo: ")
if slowo[0]=='a':
    print("Slowo zaczyna sie na pierwsza litere alfabetu")
elif slowo[0]=='z':
    print("Slowo zaczyna sie na ostatnia litere alfabetu")
else:
    print("Slowo zaczyna sie na inna litere alfabetu niz 'a' lub 'z'")