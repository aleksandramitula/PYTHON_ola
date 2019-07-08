# zakres zmiennych (global i nonlocal)

# imie = 'Jola'
# def zmien_imie():
#     imie = 'Teresa'
#
# print(imie)
# zmien_imie()
# print(imie)
# zawsze wyprintuje Jola, bo to z funkcji istnialo tylko przez chwile w momencie trwania tej funkcji.


# sprobowac to samo zrobic z nadaniem argumentu oraz z lista ??




# Dokumentowanie kodu - opis funkcji:

def dodawanie(x,y):
    """Return sum of two arguments"""
    suma=x+y
    return suma

print(dodawanie.__doc__)
