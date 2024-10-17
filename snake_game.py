from time import sleep  # Import the sleep function to control the game speed
from turtle import Screen  # Import the Screen class to create the game window
from food import Food  # Import the Food class from the food module
from score import Score  # Import the Score class from the score module
from snake import *  # Import all classes and functions from the snake module

# Function to start the snake game
def snake_game_start():
    # Setup the game window
    window = Screen()  # Create a new window object
    window.title("Snake game in Python By Aishik Mukherjee 😎")  # Set the title of the game window
    window.setup(height=700, width=700)  # Set the size of the window to 700x700
    window.bgcolor('navajo white')  # Set the background color of the window
    window.tracer(0)  # Disable automatic screen updates for smoother animations

    # Initialize the scoreboard, border, snake, and food objects
    scoreboard = Score()  # Create a Score object to manage the score display
    create_border()  # Create the game border using the function
    snake = Snake()  # Create a Snake object to manage the snake's behavior
    food = Food()  # Create a Food object to manage the food on the screen

    # Define key bindings to control the snake's movement
    window.onkey(snake.turn_up, "Up")  # Turn the snake up when the Up arrow is pressed
    window.onkey(snake.turn_down, "Down")  # Turn the snake down when the Down arrow is pressed
    window.onkey(snake.turn_left, "Left")  # Turn the snake left when the Left arrow is pressed
    window.onkey(snake.turn_right, "Right")  # Turn the snake right when the Right arrow is pressed
    window.listen()  # Start listening for key presses

    # Function to check if the snake has collided with the wall
    def wall_collision():
        # Check if the snake's head goes beyond the border on any side
        if snake.SNAKE[0].xcor() >= 330.9 or snake.SNAKE[0].xcor() <= -330.0:
            return True  # Collision with the left or right border
        elif snake.SNAKE[0].ycor() >= 290 or snake.SNAKE[0].ycor() <= -325:
            return True  # Collision with the top or bottom border
        else:
            return False  # No collision

    # Function to check if the snake has collided with itself
    def self_collision():
        # Loop through all snake segments except the head
        for body in snake.SNAKE:
            if body == snake.SNAKE[0]:  # Skip checking the head against itself
                pass
            else:
                # If the head is too close to any body segment, return True (self-collision)
                if snake.SNAKE[0].distance(body) <= 14:
                    return True

    # Main game loop
    while True:
        sleep(0.1)  # Control the speed of the game by pausing for a short time
        window.update()  # Update the screen after every move
        snake.move()  # Move the snake forward
        scoreboard.show_score()  # Display the current score

        # Check if the snake has eaten the food
        if snake.SNAKE[0].distance(food) < 16:
            snake.snake_grow()  # Grow the snake by adding a new segment
            food.generate_new_food()  # Generate a new piece of food at a random position
            scoreboard.update_scores()  # Update and display the score

        # Check if the snake has collided with the wall or itself
        if wall_collision() or self_collision():
            # If there's a collision, display the final score and end the game
            scoreboard.clear()  # Clear the screen before displaying the final score
            scoreboard.write(f"\nFinal Score = {scoreboard.live_score}", False, align="center",
                             font=('Arial', 18, 'bold'))  # Display the final score
            break  # Exit the game loop
        else:
            pass  # If no collision, continue the game

    # Close the window when the game ends
    window.exitonclick()  # Wait for a mouse click to close the game window
