#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while wall_is_beneath() == False:
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        while wall_is_on_the_left() == False:
            fill_cell()
            move_left()
    if wall_is_beneath() and wall_is_on_the_left():
        fill_cell()


if __name__ == '__main__':
    run_tasks()
