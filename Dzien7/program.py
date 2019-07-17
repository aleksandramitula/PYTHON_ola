import moj_modul
import os

print('Program wywolujacy modul:')

#moj_modul.show_dir()

print(os.listdir()) # trzeba wyprintowac wynik, bo funkcja zwraca wartosc (return)

print(moj_modul.listdir()) # nasz modul ma juz printowanie w srodku zaplecione