# 
    # 5. Method Overriding (again)
    # Here, we override the same method but with a different implementation
    # specific to a bike.
    def get_usage_type(self):
        """
        Overrides the base class method to describe a bike's specific usage.
        """
        print(f"This {self.bike_type} bike is great for exercise and short-distance travel.")


# --- Demonstration ---

print("--- Creating Vehicle Objects ---")
# Create an instance of a generic Vehicle
generic_vehicle = Vehicle("Generic", "Transporter", 2024)

# Create an instance of a Car
my_car = Car("Honda", "Civic", 2023, 4)

# Create an instance of a Bike
my_bike = Bike("Trek", "Marlin 5", 2022, "Mountain")

print("\n--- Calling Methods on Objects ---")

# Put all vehicles in a list to easily demonstrate the concept
vehicles = [generic_vehicle, my_car, my_bike]

for vehicle in vehicles:
    # The display_details() method is INHERITED from the Vehicle class
    vehicle.display_details()

    # The get_usage_type() method is called. Python automatically runs the
    # specific version from the subclass if it exists (Car, Bike),
    # or the base version if not (Vehicle). This is polymorphism.
    vehicle.get_usage_type()
    print("-" * 20) # Separator for clarity



