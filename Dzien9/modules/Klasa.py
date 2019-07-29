class Employee(object):
    """Creates new employee"""
    def __init__(self, imie, nazwisko):
        self.name = imie
        self.surname = nazwisko
    # dodanie nowej wlasciwosci:
    def say_hello(self):
        """saying hello"""
        print(f"Hello, my name is {self.name} {self.surname}")