from turtle import Turtle  # Import the Turtle class from the turtle module for graphical operations
from random import randint  # Import randint function from the random module to generate random numbers

# Define the Food class that inherits from the Turtle class
class Food(Turtle):

    # Constructor method for initializing the food object
    def __init__(self):
        super().__init__()  # Call the parent class (Turtle) constructor
        self.shape("circle")  # Set the shape of the food object to a circle
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)  # Set the size of the food (0.7 times the default size)
        self.penup()  # Lift the pen to prevent drawing when the object moves
        self.color('blue')  # Set the color of the food to blue
        self.speed("fastest")  # Set the movement speed to the fastest
        # Teleport (move) the food to a random position within the specified screen coordinates
        self.teleport(randint(-320, 320), randint(-280, 280))

    # Method to generate a new piece of food at a random location
    def generate_new_food(self):
        # Move the food to a new random location within the screen boundaries
        self.teleport(randint(-320, 320), randint(-280, 280))
