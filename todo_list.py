task_list = []

# while True:
#     task = input("Enter task: ")
#     task_list.append(task)

#     ask = input("Done entering task: y/n: ")
#     if ask == "y":
#         break


# for task in task_list:
#     print(task)


task_list = []


    
def writing_task(task):
    if task == "":
        return
    task_list.append(task)


def view_task():
    for i in range(len(task_list)):
        print(i+1, "-", task_list[i])
    




