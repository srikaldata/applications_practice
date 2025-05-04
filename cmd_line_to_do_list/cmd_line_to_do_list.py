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


# fn to load existing tasks from the txt file into the memory
def load_tasks():
    with open('tasks.txt', 'r') as task_file:
        tasks = task_file.readlines()

        for task in tasks:
            task = task.strip().split('||')
            task_list.append(task)


# fn to save a task's status update in the txt file
def save_tasks_status():
    with open('tasks.txt', 'w') as task_file:
        
        for task_name, task_description, task_status in task_list:
            content = f'{task_name}||{task_description}||{task_status}\n'
            task_file.write(content)


# to update the status of the task
def update_task_status(task_index, task_new_status):
    task = task_list[task_index]
    task[2] = task_new_status
    save_tasks_status()
    print(f'{task[0]} --> task status updated successfully!')


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

# cmd line interface to interact with the to do list:
# check if the second element is 'add' and if the num of elems is 4 (for validation)
if sys.argv[1] == 'add' and len(sys.argv) == 4:
    task_name, task_description = sys.argv[2], sys.argv[3]
    add_task(task_name, task_description)
    
elif sys.argv[1] == 'list':
    load_tasks()
    print_list_of_tasks()
    task_list= []

elif sys.argv[1] == 'update' and len(sys.argv) == 4:
    load_tasks()
    task_index, task_status = int(sys.argv[2]), sys.argv[3]
    update_task_status(task_index, task_status)
 