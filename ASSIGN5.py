# 5. Method Overriding (again)
    # Here, we override the same method but with a different implementation
    # specific to a bike.
    def get_usage_type(self):
        """
        Overrides the base class method to describe a bike's specific usage.
        """
        print(f"This {self.bike_type} bike is great for exercise and short-distance travel.")
