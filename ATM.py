from todo_list import *


while True:
    task_input = input("Enter task: ")
    writing_task(task=task_input)


    ask = input("Continue y/n: ")
    if ask == "n":
        break


view_task()

