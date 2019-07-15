import os

def listdir():
    pliki = os.listdir()
    list = []
    if len(pliki) == 0:
        return ("Katalog jest pusty")

    for obiekt in pliki:
        if os.path.isfile(obiekt):
            list.append(f"Plik: {obiekt} \n")
            #x=str(f"Pliki: {obiekt}")
        elif os.path.isdir(obiekt):
            list.append(f"Katalog: obiekt \n")
            #x=str(f"Katalog: {obiekt}")
    return list


# # aby ten kod powyzej zadzialal dobrze, to trzeba w wywolaniu funkcji zastosowac taki rodzaj printa (aby ladnie podzielilo liste na linie):
# results=moj_modul.listdir()
# for item in results:
#     print(item)



## SPOSOB NA STRINGACH:

def listdir():
    pliki = os.listdir()
    str_list = ''
    if len(pliki) == 0:
        return ("Katalog jest pusty")

    for obiekt in pliki:
        if os.path.isfile(obiekt):
            str_list += (f"Plik: {obiekt}\n")
        elif os.path.isdir(obiekt):
            str_list += (f"Katalog: {obiekt}\n")
    return str_list
