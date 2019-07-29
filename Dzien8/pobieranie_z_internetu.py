import requests
import csv
import folium # modul do robienia map

# 1) sciagniecie danych z internetu

def download_data():
    data_url='https://raw.githubusercontent.com/infoshareacademy/isa-python12/master/Day8/exercises/airports.csv?token=AGMZVYOFLTW6SJTOMBVPTRS5HCKJ2'

    airports_data = requests.get(data_url)

    #print(airports_data.content)

    #csv_data=airports_data.content
    csv_data=airports_data.text
    # airports_data.content - zwraca zawartosc w formacie binarnym - aby zapisac do csv trzeba zmienic na .text

    # Zapis sciagnietego pliku do formatu CSV:

    # 2) zapis do CSV

    csv_filename='airports.csv'

    with open(csv_filename, 'w') as csv_file:
        csv_file.write(csv_data)

download_data()


# 3) przygotowanie mapy, aby pozniej do niej zapisac nasze dane:
# 4) odczyt CSV
# zaczytanie tylko czesci atrybutow z csv


# stworzenie pustej mapy swiata:
map=folium.Map()


with open ('airports.csv','r') as csv_file:
    data = csv.reader(csv_file) # przeglada linijka po linijce plik csv, iterowalna
    for airport in data: # kazdy wiersz pliku to osobna lista
        #airport[1] - nazwa lotniska
        #airport[5] - wspolrzedne
        #airport[6] - wspolrzedne
        icon = folium.Icon(icon='plane', prefix='fa', color="gray")  # fa - font awesome https://fontawesome.com/
        point=folium.Marker(location=[airport[5],airport[6]], tooltip=airport[1], icon=icon) # stworzenie markerow (punktow)
        map.add_child(point) # dodanie nowego elementu do naszej pustej mapy

# zapis do mapy html:
map.save('map.html')


# 5) wyslanie na maila:


import smtplib #pozwala logowac sie i wysylac maile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #nasza wiadomosc bedzie sie skladala z tekstu oraz zalacznikow

#tworzymy obiekt MIMEMultipart, który za nas dokona odpowiedniego utworzenia źródła maila do wysłania
msg = MIMEMultipart()

#otwieramy plik którego zawartość chcemy wysłać jako treść maila
textfile = 'airports.csv'
map = 'map.html'
with open(textfile, 'r') as fp:
    #tworzymy obiekt MIMEText w paramatrze podając zawartość pliku
    #jest to obiekt odpowiadający za treść maila
    text = MIMEText(fp.read())

#dołączamy treść maila do naszej wiadomości
msg.attach(text)
msg.attach(map)

#ustawiamy nagłówki niezbędne do poprawnej wysyłki maila
#temat
msg['Subject'] = 'The contents of ' + textfile
#nadawca
msg['From'] = 'isapy@o2.pl'
#odbiorca
msg['To'] = 'mail@gmail.com'

#tworzymy obiekt dzięki któremy wyślemy wiadomość
#w konstruktorze podajemy adres serwera dzięki któremy będziemy wysyłać wiadomość
s = smtplib.SMTP('poczta.o2.pl')

#podany serwer wymaga uwierzytelnienia więc wywołujemy metodę do logowania
s.login('isapy@o2.pl', 'isapython')

#wywłamy wiadomość, moetoda msg.as_string() zamienia obiekt MIMEMultipart ze wszystkim załącznikami
#na wiadomość zgodną z RFC do wysłania wiadomośći
s.sendmail(msg['From'], [msg['To']], msg.as_string())

#zamykamy nasze połaczenie z serwerem
#analogicznie do otwierania plików można użyć tutaj konstrukcji with-as
#dzięki czemu s.quit() wykona się samo po wyjściu z bloku with i nie trzeba tej metody jawnie wykonywać
s.quit()