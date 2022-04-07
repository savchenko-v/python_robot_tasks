#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        while wall_is_beneath() == False:
            move_down()
        while wall_is_beneath() and wall_is_on_the_left() == False:
             move_left()
        while wall_is_beneath() and wall_is_on_the_right() == False:
            move_right()
        if wall_is_beneath() == False:
            move_down()
        else:
            break
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
