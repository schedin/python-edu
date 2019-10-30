'''

'''

class Vehicle(object):
    def __init__(self, country, origin):
        self._country = country
        self.origin = origin
        self._speed = 0

    def accel(self, increase):
        self._speed += increase

    def decel(self, decrease):
        self._speed -= decrease

