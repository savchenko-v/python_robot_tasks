#!/usr/bin/python3

from pyrob.api import *


def step():
    if wall_is_above() == False:
        move_up()
        fill_cell()
        move_down()
    if wall_is_beneath() == False:
        move_down()
        fill_cell()
        move_up()

@task
def task_8_10():
    while wall_is_on_the_right() == False:
        step()
        move_right()
        step()




if __name__ == '__main__':
    run_tasks()
