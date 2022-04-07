#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    ax = 0
    count = 0
    while wall_is_on_the_right() == False:
        if wall_is_on_the_right() == False:
            move_right()
            if wall_is_on_the_right():
                move_left()
                fill_cell()
                move_right()
                break
            else:
                move_left()
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        move_right()
        while wall_is_above() == False:
            move_up()
            if wall_is_on_the_left():
                if cell_is_filled():
                    count += 1
                    mov(ax, count)
                #     move_up()
                else:
                    fill_cell()
        while wall_is_beneath() == False:
            move_down()


if __name__ == '__main__':
    run_tasks()
