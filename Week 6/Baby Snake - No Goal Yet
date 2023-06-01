from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
ORIGIN = 0
DELAY = 0.1
SNAKE_COLOR = "blue"

def main():
    
    # Create a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Set up and launch the "snake" at point of "ORIGIN", e.g. (0, 0)
    create_and_run_snake(canvas, ORIGIN)
    
    # Final message, after game is finished (either Won, or Lost)
    print('Thank you for playing Baby Snake!\n')

def create_and_run_snake(canvas, point):
    
    # Starting from (0, 0):
    left_x = point
    right_x = point + SIZE
    top_y = point
    bottom_y = point + SIZE
    
    # Let's draw the initial frame, at the "ORIGIN", before we "animate" anything:
    snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
    
    # Show this initial frame with the same delay as the animation loop (below)
    time.sleep(DELAY)
    
    # Set the initial animation direction for the movement (if no key is pressed):
    movement_direction = "right"
    
    # Decide on how much to move the square by each frame (why not 20?):
    offset = SIZE
    
    # Keep track of game state:
    game_on = True
    
    # Define variables to keep track of the location of the snake (for collision detection):
    current_left_x = canvas.get_left_x(snake)
    current_top_y = canvas.get_top_y(snake)
    
    # Clear canvas after animation has been shown (so there is no "tail" of the snake)
    canvas.delete(snake)

    # This is the main animation loop:
    while game_on == True:
        
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
        elif movement_direction == "right":
            left_x = left_x + offset
            right_x = right_x + offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Detect a collision with the left wall while moving left (ends the game):
        elif movement_direction == "left" and current_left_x == 0:
            print('\nGame Over! \n(Left wall hit)\n')
            game_on = False
        
        # Normal change of direction to the left (game continues):   
        elif movement_direction == "left":
            left_x = left_x - offset
            right_x = right_x - offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Detect a collision with the top wall while moving up (ends the game):
        elif movement_direction == "up" and current_top_y == 0:
            print('\nGame Over! \n(Top wall hit)\n')
            game_on = False
            
        # Normal change of direction to go up (game continues) 
        elif movement_direction == "up":
            # Normal change of direction, game continues
            top_y = top_y - offset
            bottom_y = bottom_y - offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        # Detect a collision with the bottom wall while moving down
        elif movement_direction == "down" and current_top_y == CANVAS_HEIGHT - 20:
            print('\nGame Over! \n(Bottom wall hit)\n')
            game_on = False
        
        # Normal change of direction towards the bottom (game continues): 
        elif movement_direction == "down":
            top_y = top_y + offset
            bottom_y = bottom_y + offset
            snake = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, SNAKE_COLOR)
        
        else:
            pass
        
        # "Animation" delay here:
        time.sleep(DELAY)
        
        # Store the last location of the snake, to detect potential collisions in next cycle:
        current_left_x = canvas.get_left_x(snake)
        current_top_y = canvas.get_top_y(snake)
        
        # Clear canvas after animation has been shown (so there is no "tail" of the snake)
        canvas.delete(snake)


if __name__ == '__main__':
    main()
