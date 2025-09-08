# Question 1:
# ASHLEIGH N M R244588H


# Python Assignment: Class Hierarchy and Method Overriding

# 1. Base Class (Parent Class)
# This is the general class that defines common properties and methods.
class Vehicle:
    """
    A base class representing a generic vehicle.
    """
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        """
        A method to display the common details of the vehicle.
        This method will be inherited by the subclasses.
        """
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def get_usage_type(self):
        """
        A method that defines the general usage of a vehicle.
        This is the method we will OVERRIDE in our subclasses.
        """
        print("This vehicle is used for general transportation.")

