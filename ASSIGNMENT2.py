#Question 2:
# Python Assignment: Polymorphism with Shapes

import math
from abc import ABC, abstractmethod

# 1. Abstract Base Class (The "Contract")
# We define a blueprint for what a "Shape" should be.
# Any class that inherits from Shape MUST provide an 'area' method.
class Shape(ABC):
    """
    An abstract base class for all shapes, ensuring that any subclass
    will have an area() method.
    """
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape. This method must be implemented
        by any subclass.
        """
        pass



# 2. Concrete Implementations of Shapes
# Each class inherits from Shape and provides its own specific
# implementation of the area() method.

class Rectangle(Shape):
    """Represents a rectangle with a specific width and height."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

class Circle(Shape):
    """Represents a circle with a specific radius."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    """Represents a triangle with a specific base and height."""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Calculates the area of the triangle."""
        return 0.5 * self.base * self.height



# 3. The Polymorphic Function
# This function takes a list of objects. It doesn't care if they are
# Circles, Rectangles, or Triangles. It only cares that each object
# has an .area() method it can call. This is polymorphism in action.

def calculate_total_area(shapes_list):
    """
    Calculates the total area of a list of shape objects.

    Args:
        shapes_list: A list where each item is an object that
                     has an .area() method (e.g., Circle, Rectangle).

    Returns:
        The sum of the areas of all shapes in the list.
    """
    total_area = 0
    print("--- Calculating Areas ---")
    for shape in shapes_list:
        # Here is the polymorphism:
        # Python calls the correct .area() method for each object.
        # It calls Circle.area() for a Circle object, Rectangle.area() for a Rectangle, etc.
        shape_area = shape.area()
        print(f"Area of {shape.__class__.__name__}: {shape_area:.2f}")
        total_area += shape_area
    return total_area


# --- Demonstration ---

# Create a list containing different types of shape objects.
shapes = [
    Rectangle(10, 5),    # Area: 50
    Circle(7),           # Area: ~153.94
    Triangle(8, 6),      # Area: 24
    Circle(3)            # Area: ~28.27
]

# Call the function with the list of mixed shapes.
# The function works because all objects in the list adhere to the "Shape" contract.
total = calculate_total_area(shapes)

print("\n--------------------------------")
# The '.2f' formats the number to two decimal places for cleaner output.
print(f"The total area of all shapes is: {total:.2f}")








# Question 3:

#Using super() in a Class Hierarchy ---

# 1. Base Class (Parent)
class Shape:
    """
    A base class that provides some initial setup logic.
    """
    def __init__(self, shape_name):
        # This is the constructor logic we want to reuse.
        # It initializes the object by setting its name.
        print(f"--- (From Shape __init__) Initializing a new shape named '{shape_name}'. ---")
        self.shape_name = shape_name

    def calculate_area(self):
        # The base class's method. As requested, it doesn't do a full calculation,
        # but we'll have it print a message to show when it's being called.
        print(f"--- (From Shape calculate_area) Base area calculation started for {self.shape_name}. ---")
        # In a real scenario, this might perform logging or a default action.
        return 0

# 2. Derived Class (Child)
class Rectangle(Shape):
    """
    A derived class that inherits from Shape and uses super()
    to access the parent's methods.
    """
    def __init__(self, width, height):
        # --- CORRECT USAGE OF super() TO CALL THE PARENT CONSTRUCTOR ---
        # We call the parent's __init__ method to run its setup logic.
        # We must do this from within the child's __init__ method.
        # We pass "Rectangle" up to the Shape constructor.
        super().__init__("Rectangle")

        # Now, we run the initialization logic specific to the Rectangle.
        print("--- (From Rectangle __init__) Initializing Rectangle-specific attributes. ---")
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Overrides the parent's calculate_area method.
        It first calls the parent's version using super() and then
        adds its own specific calculation logic.
        """
        # --- USING super() TO CALL THE PARENT'S VERSION OF THIS METHOD ---
        # This calls the calculate_area() method from the Shape class.
        super().calculate_area()

        # Now, we perform the specific calculation for the Rectangle.
        print(f"--- (From Rectangle calculate_area) Calculating area for {self.width}x{self.height}. ---")
        area = self.width * self.height
        return area

# --- Demonstration ---

print("Creating a Rectangle object...")
# When this line runs, both the Shape and Rectangle __init__ methods will be executed.
my_rectangle = Rectangle(10, 7)

print("\n" + "="*50 + "\n")

print("Calling the calculate_area() method on the Rectangle object...")
# This will first execute the print statement from Shape.calculate_area()
# and then perform the calculation from Rectangle.calculate_area().
calculated_area = my_rectangle.calculate_area()

print("\n" + "="*50 + "\n")

print(f"Final calculated area of the rectangle is: {calculated_area}")








# Question 4:

class Dog:
    def make_sound(self):
        print("Woof!")

class Cat:
    def make_sound(self):
        print("Meow!")

def process_sound(sound_object):
    """
    This function processes an object that has a make_sound() method.
    It doesn't need to know the specific type of the object.
    """
    sound_object.make_sound()

# Create instances of Dog and Cat
dog_instance = Dog()
cat_instance = Cat()

# Call the process_sound function with both instances
print("Processing the dog object:")
process_sound(dog_instance)

print("\nProcessing the cat object:")
process_sound(cat_instance)

# To show how flexible this is, let's create another class.
class Duck:
    def make_sound(self):
        print("Quack!")

duck_instance = Duck()
print("\nProcessing the duck object:")
process_sound(duck_instance)








#Question 5:

import abc

# 1. Define the Abstract Base Class (ABC) for FileHandler
class FileHandler(abc.ABC):
    """
    Abstract Base Class for file handling.
    All concrete file handler classes must implement read() and write() methods.
    """

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def read(self):
        """
        Abstract method to read content from the file.
        Concrete classes must implement this.
        """
        pass

    @abc.abstractmethod
    def write(self, data):
        """
        Abstract method to write content to the file.
        Concrete classes must implement this.
        """
        pass

    def get_filename(self):
        """
        A concrete method that can be inherited directly by subclasses.
        """
        return self.filename

# 2. Create a Concrete Class for Text Files
class TextFileHandler(FileHandler):
    """
    Concrete implementation for handling text files.
    It implements the abstract read() and write() methods for text data.
    """
    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Reading text from '{self.filename}':\n{content}")
                return content
        except FileNotFoundError:
            print(f"Text file '{self.filename}' not found.")
            return None
        except Exception as e:
            print(f"Error reading text file '{self.filename}': {e}")
            return None

    def write(self, data):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(data)
                print(f"Successfully wrote text to '{self.filename}'.")
        except Exception as e:
            print(f"Error writing to text file '{self.filename}': {e}")

# 3. Create a Concrete Class for Binary Files
class BinaryFileHandler(FileHandler):
    """
    Concrete implementation for handling binary files.
    It implements the abstract read() and write() methods for binary data.
    """
    def read(self):
        try:
            with open(self.filename, 'rb') as f:
                content = f.read()
                print(f"Reading binary data from '{self.filename}': {content[:50]}...") # Show first 50 bytes
                return content
        except FileNotFoundError:
            print(f"Binary file '{self.filename}' not found.")
            return None
        except Exception as e:
            print(f"Error reading binary file '{self.filename}': {e}")
            return None

    def write(self, data):
        if not isinstance(data, bytes):
            print("Error: BinaryFileHandler expects bytes data.")
            return

        try:
            with open(self.filename, 'wb') as f:
                f.write(data)
                print(f"Successfully wrote binary data to '{self.filename}'.")
        except Exception as e:
            print(f"Error writing to binary file '{self.filename}': {e}")

# --- Demonstration ---
if __name__ == "__main__":
    text_file_name = "example.txt"
    binary_file_name = "example.bin"

    # Demonstrate TextFileHandler
    print("--- Demonstrating TextFileHandler ---")
    text_handler = TextFileHandler(text_file_name)
    text_handler.write("Hello, this is a test for the text file handler.\nIt works with strings.")
    text_handler.read()
    print(f"Filename via inherited method: {text_handler.get_filename()}\n")

    # Demonstrate BinaryFileHandler
    print("--- Demonstrating BinaryFileHandler ---")
    binary_handler = BinaryFileHandler(binary_file_name)
    binary_data = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A' * 5 # Some sample binary data
    binary_handler.write(binary_data)
    binary_handler.read()
    print(f"Filename via inherited method: {binary_handler.get_filename()}\n")