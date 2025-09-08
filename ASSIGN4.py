# 4. Another Subclass
# This class also inherits from Vehicle but has different features than Car.
class Bike(Vehicle):
    """
    A subclass representing a bike. It also inherits from Vehicle.
    """
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type # Attribute specific to Bike
