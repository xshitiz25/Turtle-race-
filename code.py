import turtle
import time
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
TURTLE_COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def display_message(message, pen):
    pen.clear()
    pen.penup()
    pen.goto(0, SCREEN_HEIGHT // 2 - 40)
    pen.write(message, align="center", font=("Arial", 14, "normal"))

def prompt_racers():
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.hideturtle()

    while True:
        try:
            racers = int(screen.textinput("Number of Racers", "Enter the number of racers (2-10):"))
            if 2 <= racers <= 10:
                pen.clear()  # Clear any previous messages
                return racers
            else:
                display_message('Please enter a number between 2 and 10.', pen)
        except ValueError:
            display_message('Invalid input. Please enter a number.', pen)

def start_race(colors):
    competitors = setup_turtles(colors)

    while True:
        for competitor in competitors:
            competitor.forward(random.randint(1, 20))

            if competitor.ycor() >= SCREEN_HEIGHT // 2 - 10:
                winning_color = competitor.fillcolor()
                return winning_color

def setup_turtles(colors):
    turtles = []
    spacing = SCREEN_WIDTH // (len(colors) + 1)
    
    for idx, color in enumerate(colors):
        new_turtle = turtle.Turtle()
        new_turtle.color(color)
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setheading(90)
        new_turtle.goto(-SCREEN_WIDTH//2 + (idx + 1) * spacing, -SCREEN_HEIGHT//2 + 20)
        new_turtle.pendown()
        turtles.append(new_turtle)
    
    return turtles

def initialize_screen():
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title('Exciting Turtle Race!')
    # Get the Tkinter root window and set its position
    root = screen.getcanvas().winfo_toplevel()
    root.lift()  # Bring window to the top
    root.attributes('-topmost', True)  # Set as topmost window
    root.attributes('-topmost', False)  # Reset topmost attribute

def display_winner(winner):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()

    # Define the message and font
    message = f"Congratulations! The winning turtle is: {winner}"
    font = ("Arial", 16, "bold")

    # Move to the position where the text will be displayed
    pen.goto(0, 0)

    # Draw a rectangle around the text
    pen.color("black", "lightyellow")
    pen.begin_fill()
    text_width = 500  # Width of the rectangle
    text_height = 50  # Height of the rectangle
    pen.goto(-text_width / 2, text_height / 2)
    pen.pendown()
    for _ in range(2):
        pen.forward(text_width)
        pen.right(90)
        pen.forward(text_height)
        pen.right(90)
    pen.end_fill()
    pen.penup()

    # Move to the center and display the text
    pen.goto(0, -10)  # Adjust position for better centering
    pen.write(message, align="center", font=font)

def main():
    num_racers = prompt_racers()
    random.shuffle(TURTLE_COLORS)
    selected_colors = TURTLE_COLORS[:num_racers]
    
    initialize_screen()
    winner = start_race(selected_colors)
    
    display_winner(winner)
    time.sleep(5)

if __name__ == "__main__":
    main()
