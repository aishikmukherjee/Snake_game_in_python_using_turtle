from turtle import Turtle  # Import the Turtle class for graphical operations

# Constants
STARTING_SNAKE_PARTS_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for snake segments
MOVE_DISTANCE = 20  # Distance the snake moves in each step


# Function to create a border around the playing area
def create_border():
    border = Turtle()  # Create a new Turtle object for the border
    border.color('black')  # Set the border color to black
    border.width(1)  # Set the borderline width
    border.hideturtle()  # Hide the turtle cursor so only the line is visible
    border.speed('fastest')  # Set the speed of drawing to the fastest
    # Start drawing the border (move the turtle without drawing)
    border.teleport(-330, 290)  # Position the turtle to the top-left corner
    border.forward(660)  # Draw the top horizontal line
    border.right(90)  # Turn 90 degrees to the right
    border.forward(620)  # Draw the right vertical line
    border.right(90)  # Turn 90 degrees to the right
    border.forward(660)  # Draw the bottom horizontal line
    border.right(90)  # Turn 90 degrees to the right
    border.forward(620)  # Draw the left vertical line


# Class to define the behavior of the snake
class Snake:

    # Constructor method to initialize the snake
    def __init__(self):
        self.SNAKE = []  # List to store all snake segments
        self.create_snake()  # Create the initial snake

    # Method to create the initial snake by adding segments at predefined positions
    def create_snake(self):
        for position in STARTING_SNAKE_PARTS_POSITIONS:
            self.add_snake_parts(position)  # Add each part of the snake

    # Method to add a new segment to the snake at a specific position
    def add_snake_parts(self, position):
        segment = Turtle("square")  # Create a square turtle for the snake's segment
        segment.color("lime green")  # Set the color of the snake to lime green
        segment.penup()  # Lift the pen to prevent drawing when the segment moves
        segment.goto(position)  # Move the segment to the specified position
        self.SNAKE.append(segment)  # Add the new segment to the snake's list

    # Method to grow the snake by adding a new segment at the position of the last segment
    def snake_grow(self):
        self.add_snake_parts(self.SNAKE[-1].position())  # Add a segment at the last segment's position

    # Method to move the snake forward
    def move(self):
        self.SNAKE[0].color('deep pink')  # Color the head of the snake differently for visibility
        # Move each segment to the position of the segment in front of it, starting from the tail
        for part_number in range(len(self.SNAKE) - 1, 0, -1):
            new_x = self.SNAKE[part_number - 1].xcor()  # Get the x-coordinate of the segment ahead
            new_y = self.SNAKE[part_number - 1].ycor()  # Get the y-coordinate of the segment ahead
            self.SNAKE[part_number].goto(new_x, new_y)  # Move the current segment to the new position
        self.SNAKE[0].forward(MOVE_DISTANCE)  # Move the head of the snake forward

    # Method to turn the snake upwards (90 degrees)
    def turn_up(self):
        if self.SNAKE[0].heading() != 270:  # Prevents turning upwards if the snake is moving downwards
            self.SNAKE[0].setheading(90)  # Set the snake's direction to up

    # Method to turn the snake downwards (270 degrees)
    def turn_down(self):
        if self.SNAKE[0].heading() != 90:  # Prevents turning downwards if the snake is moving upwards
            self.SNAKE[0].setheading(270)  # Set the snake's direction to down

    # Method to turn the snake left (180 degrees)
    def turn_left(self):
        if self.SNAKE[0].heading() != 0:  # Prevents turning left if the snake is moving right
            self.SNAKE[0].setheading(180)  # Set the snake's direction to left

    # Method to turn the snake right (0 degrees)
    def turn_right(self):
        if self.SNAKE[0].heading() != 180:  # Prevents turning right if the snake is moving left
            self.SNAKE[0].setheading(0)  # Set the snake's direction to right
