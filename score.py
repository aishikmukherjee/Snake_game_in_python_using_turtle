from turtle import Turtle  # Import the Turtle class for graphical operations


# Define the Score class that inherits from the Turtle class
class Score(Turtle):

    # Constructor method for initializing the score object
    def __init__(self):
        super().__init__()  # Call the parent class (Turtle) constructor
        self.live_score = 0  # Initialize the player's score to 0
        self.hideturtle()  # Hide the turtle cursor to only display the score text
        self.teleport(0, 300)  # Position the score at the top center of the screen
        self.color('black')  # Set the text color to black

    # Method to display the current score on the screen
    def show_score(self):
        """Displays the Scores of the player"""
        self.clear()  # Clear the previous score before displaying the updated score
        # Write the current score on the screen, aligned to the center, using Arial font
        self.write(f"\nCurrent Score = {self.live_score}", False, align="center", font=('Arial', 18, 'bold'))

    # Method to update the player's score
    def update_scores(self):
        """Updates the players live score"""
        self.live_score += 1  # Increment the player's score by 1
        self.show_score()  # Display the updated score
