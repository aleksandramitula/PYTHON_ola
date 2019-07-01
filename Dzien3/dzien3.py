temperature = 25
#DUZYMI LITERAMI piszemy stala, nie zmienna. To sa te wartosci, ktorych nie chcemy zmieniac w srodku w kodzie, ale mozna zmienic na poczatku:
HOT_TEMPERATURE=30
WARM_TEMPERATURE=25
NOT_COLD_NOT_WARM_TEMPERATURE=20

if temperature >=HOT_TEMPERATURE:
    print("it's hot")
elif temperature >=WARM_TEMPERATURE:
    print("it's warm")
elif temperature >=NOT_COLD_NOT_WARM_TEMPERATURE:
    print("it's not warm or cold")
else:
    print("it's cold")