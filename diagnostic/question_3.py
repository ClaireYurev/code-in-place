from karel.stanfordkarel import *

def main():

    if front_is_clear():
        draw_a_wave()

    while front_is_clear():
        for i in range(2):
            move()
        draw_a_wave()

def draw_a_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    for i in range(2):
        turn_left()
    move()
    turn_left()

if __name__ == '__main__':
    main()
