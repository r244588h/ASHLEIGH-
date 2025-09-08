# 2. Subclass (Child Class)
# This class inherits from Vehicle and adds its own specific features.
class Car(Vehicle):
    """
    A subclass representing a car. It inherits from Vehicle.
    """
    def __init__(self, brand, model, year, number_of_doors):
        # 'super()' calls the __init__ method of the parent class (Vehicle)
        # to handle the common attributes.
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors # Attribute specific to Car