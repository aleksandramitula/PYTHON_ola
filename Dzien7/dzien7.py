import os

# wyprintowanie wszystkich plikow w obecnej lokalizacji
# print(os.listdir())
# Sprawdzanie, czy
# os.path.isdir()
# os.path.isfile()


# pliki=os.listdir()
#
# for obiekt in pliki:
#     if os.path.isfile(obiekt):
#         print(f"Plik: {obiekt}")
#     elif os.path.isdir(obiekt):
#         print(f"Katalog: {obiekt}")

# list=[]
#
# try:
#     list[0]
# except:
#     print('Error')
#     exit()




# # Od szczegolu do ogolu:
# # Teraz program ma problem z dzieleniem przez zero, a nie indeksem:

list=['dhhd']

# try:
#     list[0]
#     10/0
# except IndexError:
#     print('Lista jest pusta')
#     exit()
# except:
#     print('Nieznany blad')


# # Sposob z if-em:
# # 1)
# if not list:
#     print("Puste")
# # 2)
# if len(list) == 0:
#     print("Puste")



## CALOSC PROGRAMU:
import os

pliki=os.listdir()

if len(list) == 0:
    print("Katalog jest pusty")

for obiekt in pliki:
    if os.path.isfile(obiekt):
        print(f"Plik: {obiekt}")
    elif os.path.isdir(obiekt):
        print(f"Katalog: {obiekt}")
