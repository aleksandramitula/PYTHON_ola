# TWORZYMY KLASE:
# Klase nazywamy z wielkiej litery
# klasa mowi Pythonowi, w jaki sposob ma cos robic

class Employee(object):
    """Creates new employee"""
    def __init__(self, imie, nazwisko):
        self.name = imie
        self.surname = nazwisko
    # dodanie nowej wlasciwosci:
    def say_hello(self):
        """saying hello"""
        print(f"Hello, my name is {self.name} {self.surname}")



# INSTANCJA OBIEKTU, wykonanie projektu. Najczesciej to jest w osobnym pliku umieszczone:
# zeby wywolac ja w innym pliku, to nalezy wywolac jak funkcje (from Dzien9.modules.Employee import Employee)

new_employee = Employee("Mateusz", "Cebula")
another_new_employee = Employee("Jan", "Kowalski")
another_new_employee.say_hello()