# 3. Method Overriding
# We are providing a specific implementation for the get_usage_type() method
# that is different from the parent class's version.
def get_usage_type(self):
    """
    Overrides the base class method to describe a car's specific usage.
    """
    print("This car is mainly used for family trips and commuting.")