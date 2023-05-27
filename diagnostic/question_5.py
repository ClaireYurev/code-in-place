from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas, x, y)
    # ^ Added arguments canvas, x, and y into the draw_car() call

    x = 100
    y = 100
    draw_car(canvas, x, y)
    # ^ Added arguments canvas, x, and y into the draw_car() call again

def draw_car(given_canvas, given_x, given_y):
    # ^ Added parameters given_canvas, given_x, and given_y into definition
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    given_canvas.create_rectangle(given_x, given_y, given_x + 50, given_y + 20)
    given_canvas.create_rectangle(given_x + 10, given_y - 10, given_x + 40, given_y + 20)

if __name__ == '__main__':
    main()
