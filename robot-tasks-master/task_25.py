#!/usr/bin/python3

from pyrob.api import *


def func():
    move_right()
    fill_cell()
    for i in range(2):
        move_down()
        fill_cell()
    move_left()
    move_up()
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    move_left(n=2)
    move_up()


@task
def task_2_2():
    move_down()
    for i in range(4):
        func()
        move_right(n=4)
    func()




if __name__ == '__main__':
    run_tasks()
