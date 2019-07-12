# zadanie domowe dzien 2

#zad 1
#Przypisz do zmiennej o nazwie float_but_int wartosc dzielenia 50 / 2. Jakiego typu jest wynik (do sprawdzenia typu type(zmienna))?
#Sprawdz przy pomocy metody wbudowanej w otrzymany wyzej typ czy liczba jest calkowita (dokumentacja - dir(nazwa_zmiennej) lub help(typ)), dokumentacja Python


float_but_int = 50/2
print (float_but_int)
print (type(float_but_int))
print (float_but_int.is_integer())


# 2. (Kalkulator, albo Python) - liczba zapisana w systemie binarnym na 8 bitach - 11011010 to w systemie dziesietnym liczba:
#11011010

x=(0*2**0)+(1*2**1)+(0*2**2)+(1*2**3)+(1*2**4)+(0*2**5)+(1*2**6)+(1*2**7)
print(x)



#3. Przypisz do 3 zmiennych pojedyncze slowa "Sun", "is", "setting", polacz je w jeden ciag znaków, ale tak, aby kazde slowo bylo w nowej linii, kazda nowa linia ma miec jedno
#wiecej wciecie tabulatora, tak aby wygladalo to nastepujaco:
#Sun
#              is
#                             setting

a='sun'
b='is'
c='setting'

text=(a+'\n\t'+b+'\n\t\t'+c)
print(text)

#alternatywa: print(f'{a}\n\t{b}\n\t\t{c}')


#4. zapoznaj sie z metoda input() w Python - wyszukaj w dokumentacji i sprawdz dzialanie. Funkcja print zachec uzytkownika, aby podal liczbe, nastepnie wypisz kwadrat oraz szescian tej liczby
#Postaraj sie o odpowiedni wyglad odpowiedzi, opisujacy uzyskane wyniki, np.
#Szescian liczby x wynosi x^3, natomiast kwadrat x^2

y=input('Wpisz dowolna liczbe:')
y=float(y)
kwadrat=y**2
szescian=y**3
print(f'Liczba {y} podniesiona do kwadratu daje {kwadrat}, natomiast do szescianu daje {szescian}')



#5. Warunek if - przy pomocy metody input pobierz od uzytkownia wartosc temperatury. Ustaw 3 minimalne temperatury jako zmienne - zimna, ciepla, goraca
# (np. 10 stopni, 20 stopni, 30 stopni) i na podstawie temperatury podanej przez uzytkownika, wyswietl czy jest zimno, cieplo, czy goraco

x=input('Podaj temperature:')
x=float(x)
zimno=0
cieplo=15
goraco=30

if x<zimno or (x>=zimno and x<cieplo):
    print('Jest zimno')

if x>=cieplo and x<goraco:
    print('Jest cieplo')

if x>=goraco:
    print('Jest goraco')



#6. Petla while
#Oblicz silnie z podanej przez uzytkownika (metoda input) liczby - wyszukaj algorytm na silnie i napisz - przydadza sie zmienne, warunek if, operator *= (edited)
#It multiplies right operand with the left operand and assign the result to left operand 	c *= a is equivalent to c = c * a


n=input('Podaj liczbe:')
n=int(n)
wynik=1
i=1

while (i<n):
    i=i+1
    wynik=i*wynik #6

#print('i='+str(i))
#print('n='+str(n))
print('wynik='+str(wynik))