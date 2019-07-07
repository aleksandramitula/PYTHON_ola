# FUNKCJE

def dodawanie (pierwszy_el, drugi_el):
    suma=pierwszy_el+drugi_el
    return suma

wynik=dodawanie(1,3)
print(wynik)
#print(dodawanie(1,3))


# 2. Napisz funkcję, powtarzającą słowo x razy (2 parametry - slowo oraz ile razy powtorzyc) (bedzie potrzebna petla for in oraz klasa range)

def repeat_word (slowo,powtorzenia):
    for i in range(powtorzenia):
        print(slowo)

repeat_word("hej",6)


