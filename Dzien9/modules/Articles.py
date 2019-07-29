bike_types = {"cross": "Cross bicycle", "road": "Road bicycle"}

class Bike(object):
    """defines new bike"""
    def __init__(self, color, type, front_wheel, back_wheel, frame, handlebar = "fitness", seat = "classic, stock, seat"):
        """
        :param color:
        :param type:
        :param front_wheel:
        :param back_wheel:
        :param frame:
        :param handlebar:
        :param seat:
        """
        self.color = color
        self.type = type
        self.handlebar = handlebar
        self.seat = seat
        self.front_wheel = front_wheel
        self.back_wheel = back_wheel
        self.frame = frame

    def ride(self):
        """ride this bike"""
        print(f"I'm riding {self.color} bike")

    def ring(self):
        """use bicycle bell"""
        print(f"Ring ring ring!")

    # def ___str___(self):
    #     print()

class Wheel(object):
    def __init__(self, size, width, color):
        self.size = size
        self.width = width
        self.color = color

class Frame(object):
    def __init__(self, size, color, geometry):
        self.size = size
        self.color = color
        self.geometry = geometry

