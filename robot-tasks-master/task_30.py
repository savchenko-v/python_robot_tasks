#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    counter = 0
    number = 1
    while wall_is_beneath() == False:
        move_down()
        counter += 1

    while counter > number:
        for i in range(counter-number):
            move_up()
            fill_cell()
        move_up()
        for i in range(counter-number):
            move_right()
            fill_cell()
        move_right()
        for i in range(counter-number):
            move_down()
            fill_cell()
        move_down()
        for i in range(counter-number):
            move_left()
            fill_cell()
        move_up()
        number += 2

    while wall_is_beneath() == False:
        move_down()
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
