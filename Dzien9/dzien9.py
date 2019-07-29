# # INSTANCJA OBIEKTU, wykonanie projektow:
# # Wywolanie klasy jak modul.
#
# from Dzien9.modules.Employee import Employee
#
# new_employee = Employee(3000, "Mateusz", "Cebula")
# # another_new_employee = Employee(2000,"Jan", "Kowalski")
# # another_new_employee.say_hello()
# new_employee.increase_salary(10)
# print(new_employee.salary)



# BIKES EXCERSISE

from Dzien9.modules.Articles import bike_types, Bike, Frame, Wheel, ElectricBike


front_wheel = Wheel(28,3,"black")
back_wheel = Wheel(28,4,"black")
frame=Frame(19,"red","sport")


new_bike=Bike("blue",bike_types["cross"],front_wheel,back_wheel,frame)

# dodanie funkcji, co robi rower:

new_bike.ride()
new_bike.ring()

# dla chetnych zrobic, aby dzialal print
# print(new_bike)
# print(new_bike.color)



# elektryczny rower, zamiast normalnego:
electric_bike=ElectricBike("green",bike_types["cross"],front_wheel,back_wheel,frame)

electric_bike.ride()
electric_bike.ring()
electric_bike.increase_motor_power()