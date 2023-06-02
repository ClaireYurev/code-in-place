from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
SIZE = 20
SNAKE_ORIGIN_LEFT_X = 0
SNAKE_ORIGIN_TOP_Y = 0
DELAY = 0.1
SNAKE_COLOR = "blue"
TARGET_COLOR = "pink"

def main():
    
    # Create a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Set up and launch the "snake" at point of "ORIGIN", e.g. (0, 0)
    create_and_run_snake(canvas)
        
    # Final message, after game is finished (either Won, or Lost)
    print('Thank you for playing Baby Snake :)\n')
    

def create_and_run_snake(canvas):
    
    # Starting from (0, 0):
    left_x = SNAKE_ORIGIN_LEFT_X
    right_x = left_x + SIZE
    top_y = SNAKE_ORIGIN_TOP_Y
    bottom_y = top_y + SIZE
    
    # Location of target
    target_left_x = random_location()
    target_right_x = target_left_x + SIZE
    target_top_y = random_location()
    target_bottom_y = target_top_y + SIZE
    
    # Let's draw the initial frame, at the "ORIGIN", before we "animate" anything:
    snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
    
    # Let's draw the target, at its location, before we "animate" anything:
    target = canvas.create_rectangle(target_left_x, target_top_y, target_right_x, target_bottom_y, TARGET_COLOR)
    
    # Show this initial frame with the same delay as the animation loop (below)
    time.sleep(DELAY)
    
    # Set the initial animation direction for the movement (if no key is pressed):
    movement_direction = "right"
    
    # Decide on how much to move the square by each frame (why not 20?):
    offset = SIZE
    
    # Keep track of game state:
    game_on = True
    game_won = False
    celebration_in_seconds = 30
    
    # Define variables to keep track of the location of the snake (for collision detection):
    current_left_x = canvas.get_left_x(snake)
    current_top_y = canvas.get_top_y(snake)
    
    # Clear canvas after animation has been shown (so there is no "tail" of the snake)
    canvas.delete(snake)

    # This is the main animation loop:
    while game_on == True and game_won == False:
        
        # Handle key input:
        key = canvas.get_last_key_press()
        
        if key == 'ArrowRight':
            movement_direction = "right"
            print('\nright arrow pressed: ➡')
        if key == 'ArrowLeft':
            movement_direction = "left"
            print('\nleft arrow pressed: ⬅')
        if key == 'ArrowUp':
            movement_direction = "up"
            print('\nup arrow pressed: ⬆')
        if key == 'ArrowDown':
            movement_direction = "down"
            print('\ndown arrow pressed: ⬇')
        
        # Phew! All done! Now we can draw the snake. Let's handle each possible
        # direction, depending on what's inside the "movement_direction" variable
        
        # Detect a collision with the right wall while moving right (ends the game):
        if movement_direction == "right" and current_left_x == CANVAS_WIDTH - 20:
            print('\nGame Over! \n(Right wall hit)\n')
            game_on = False
            
        # Normal change of direction to the right (game continues):  
        if movement_direction == "right":
            left_x = left_x + offset
            right_x = right_x + offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Detect a collision with the left wall while moving left (ends the game):
        if movement_direction == "left" and current_left_x == 0:
            print('\nGame Over! \n(Left wall hit)\n')
            game_on = False
        
        # Normal change of direction to the left (game continues):   
        if movement_direction == "left":
            left_x = left_x - offset
            right_x = right_x - offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Detect a collision with the top wall while moving up (ends the game):
        if movement_direction == "up" and current_top_y == 0:
            print('\nGame Over! \n(Top wall hit)\n')
            game_on = False
            
        # Normal change of direction to go up (game continues) 
        if movement_direction == "up":
            # Normal change of direction, game continues
            top_y = top_y - offset
            bottom_y = bottom_y - offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Detect a collision with the bottom wall while moving down
        if movement_direction == "down" and current_top_y == CANVAS_HEIGHT - 20:
            print('\nGame Over! \n(Bottom wall hit)\n')
            game_on = False
        
        # Normal change of direction towards the bottom (game continues): 
        if movement_direction == "down":
            top_y = top_y + offset
            bottom_y = bottom_y + offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Store the last location of the snake, to detect potential collisions in next cycle:
        current_left_x = canvas.get_left_x(snake)
        current_top_y = canvas.get_top_y(snake)
        
        # Detect a win
        if current_left_x == target_left_x and current_top_y == target_top_y:
            print('\nCongratulations! You Won!\n')
            game_on = False
            game_won = True
        
        # "Animation" delay here:
        time.sleep(DELAY)
        
        # Clear canvas after animation has been shown (so there is no "tail" of the snake)
        canvas.delete(snake)
    
    while game_won == True and celebration_in_seconds > 0:
        # Clear canvas 
        canvas.delete(snake)
        
        # Let's draw the target, at its location, before we "animate" anything:
        win = canvas.create_rectangle(current_left_x, current_top_y, current_left_x + SIZE, current_top_y + SIZE, random_color())
        
        # Adjust the countdown timer:
        celebration_in_seconds -= 1
        
        # "Animation" delay here:
        time.sleep(DELAY)

def random_color():
    colors = ['purple', 'red', 'green', 'yellow', 'cyan', 'orange', 'pink']
    return random.choice(colors)

def random_location():
    # The locations are done in increments of 20 pixels, based on the SIZE constant
    locations = []
    

    # We choose to assume that the canvas is SQUARE. I.e. the HEIGHT equals LENGTH.
    # This is why we define possible_locations variable inside the "if" statement.
    # This is done on purpose, so that if the canvas is NOT square, we'll get an error, and the game won't run.
    
    if CANVAS_HEIGHT == CANVAS_WIDTH:
        
        possible_locations = CANVAS_HEIGHT / SIZE - 1
        """
            Above, you'll notice the "- 1". This subtraction of 1 is done on purpose:
            We choose to not include the possibility of the Target being placed at 0,0.
            To illustrate this, uncomment line 196 (the 'print(locations)' line).
            You will see the following:
            [20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 280.0]
            In other words, there is no location at  "0.0", in the above list.
            Please try to run the same, but without the "- 1", i.e. "possible_locations = CANVAS_HEIGHT / SIZE"
            In that case, without the "- 1", you would see the following:
            [0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 280.0]
            Control this as you wish :)
        """
    
    while possible_locations > 0:
        locations.append(CANVAS_HEIGHT - SIZE * possible_locations)
        possible_locations -= 1
    
    #print(locations)
    
    return random.choice(locations)

if __name__ == '__main__':
    main()
