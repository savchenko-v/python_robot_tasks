#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    n = 1
    for i in range(13):
        for j in range(n):
            move_right()
            fill_cell()
        move_left(n=n)
        move_down()
        n += 1
    move_right()



if __name__ == '__main__':
    run_tasks()
