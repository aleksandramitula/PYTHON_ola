# TWORZYMY KLASE:
# Klase nazywamy z wielkiej litery
# klasa mowi Pythonowi, w jaki sposob ma cos robic

class Employee(object):
    """Creates new employee"""

    def __init__(self, salary, imie, nazwisko = "Kowalski"):
        self.name = imie
        self.surname = nazwisko
        self.salary = salary

    def say_hello(self):
        """saying hello"""
        print(f"Hello, my name is {self.name} {self.surname}")

    def increase_salary(self, percentage):
        """increase salary"""
        self.salary = (1 + percentage/100) * self.salary

