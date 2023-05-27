from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas, x, y)

    x = 100
    y = 100
    draw_car(canvas, x, y)

def draw_car(given_canvas, given_x, given_y):
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    given_canvas.create_rectangle(given_x, given_y, given_x + 50, given_y + 20)
    given_canvas.create_rectangle(given_x + 10, given_y - 10, given_x + 40, given_y + 20)

if __name__ == '__main__':
    main()
