import vehicle

class Tank(vehicle.Vehicle):
    def __init__(self, country, origin):
        vehicle.Vehicle.__init__(self, country, origin)
        
        self._direction = 0
        self._location = {'x': 0, 'y': 0}
        self._shells = 20
        self._health = 100

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        
    def rotate_right(self, degrees):
        self._direction += degrees % 360        
        
    def shoot(self):
        self._shells -= 1

    def take_damage(self, amount):
        self._health -= amount
        
    # Example of operator overloading
    def __add__(self, other): 
        return self._health + other._health
    
    def __str__(self):
        return f" _speed {self._speed}, _health {self._health} and _location {self._location}"

    @property
    def tank_health(self):
        return self._health
    
    @tank_health.setter
    def tank_health(self, health):
        self._health = health



