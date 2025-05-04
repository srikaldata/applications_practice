# importing packages
import sys

# initializing an empty task list
task_list = []


# fn to save the task in a txt file
def save_tasks():
    with open('tasks.txt', 'a') as task_file:
        
        for task_name, task_description, task_status in task_list:
            content = f'{task_name}||{task_description}||{task_status}\n'
            task_file.write(content)


# function to add and save the task in a txt file
def add_task(task_name, task_description):

    task_list.append([task_name, task_description, 'PENDING'])
    print(f'Task {task_name} is successfully added!')
    save_tasks()
