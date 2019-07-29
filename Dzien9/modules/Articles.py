bike_types = {"cross":"Cross bicycle", "road":"Road bicycle"}

class Bike(object):
    def __init__(self, color, type):
        self.color = color
        self.type = type


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