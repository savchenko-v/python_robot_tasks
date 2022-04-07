#!/usr/bin/python3

from pyrob.api import *

def func():
    i = 1
    while wall_is_on_the_right() == False:
        for j in range(i):
            move_right(i)
            fill_cell()
            i += 1

@task
def task_7_5():
    flag = False
    step = 1

    move_right()
    fill_cell()
    while flag == False:
        move_right(step)
        if wall_is_on_the_right():
            flag = True
            # fill_cell()
        # step = move_right()
        fill_cell()
        step += 1
    # func()


if __name__ == '__main__':
    run_tasks()
