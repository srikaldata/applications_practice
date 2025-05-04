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


# fn to print the existing list of tasks in the command line
def print_list_of_tasks():
    for idx, task in enumerate(task_list):
        print(f"{idx} {' '.join(task)}")



# loading any existing tasks, if any, which exists in tasks.txt
load_tasks()

# print the tasks in the task_list
print_list_of_tasks()

# add_task('Buy breakfast', '2 eggs scrambled, orange juice')
# add_task('Buy lunch', 'greek salad, hummus, pita bread')
# add_task('Hit the gym', 'cardio: jog 20 mins')
# add_task('Hit the gym', 'weights: bicep curls, dead lift, bench press')
# add_task('End of day', 'meditate')
# add_task('End of day', 'sleep')
# print(task_list)

