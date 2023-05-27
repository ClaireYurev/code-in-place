from graphics import Canvas
import time
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.00001

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

def main():
    
    counter = 0
    
    time.sleep(1)
    
    mouse_is_on = True
    
    while mouse_is_on:
        draw_circle(canvas)
        counter = counter + 1
        print("Program has been running for:", counter, "cycles.")
        time.sleep(DELAY)
        mouse_is_on = mouse_is_on_canvas()
    
    print("Mouse cursor exited the canvas on the " + str(counter) + "'th cycle.")

def mouse_is_on_canvas():
    
    if x_is_on_canvas() and y_is_on_canvas():
        return True
        
    return False

def x_is_on_canvas():
    
    if canvas.get_mouse_x() > -1 and canvas.get_mouse_x() < CANVAS_WIDTH - 1:
        return True
        
    return False

def y_is_on_canvas():
    
    if canvas.get_mouse_y() > -1 and canvas.get_mouse_y() < CANVAS_HEIGHT - 1:
        return True
        
    return False
    
def draw_circle(canvas):
    
    x = canvas.get_mouse_x()
    y = canvas.get_mouse_y()
    rx = x + CIRCLE_SIZE
    by = y + CIRCLE_SIZE
    
    canvas.create_oval(x, y, rx, by, random_color())

def random_color():
    colors = ["forestgreen", "pink", "purple", "blue", "lightblue", "cyan"]
    return random.choice(colors)

if __name__ == "__main__":
    main()
