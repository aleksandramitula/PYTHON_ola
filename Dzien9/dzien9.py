# Wywolanie klasy jak modul.

from Dzien9.modules.Klasa import Employee

new_employee = Employee("Mateusz", "Cebula")
another_new_employee = Employee("Jan", "Kowalski")
another_new_employee.say_hello()