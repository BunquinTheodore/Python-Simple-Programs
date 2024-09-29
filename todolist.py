task_list = []

def add_task(task, task_list):
    task_list.append(task)
    print ("Task Added Successfully!")
    print("\nTo-do list: ",task_list)

def view_task (task_list):
    if not task_list:
        print ("No task found")
    else:
        print ("Tasks: ")
        for i, task in enumerate (task_list, 1):
            print (f"{1}.{task}")

def mark_task_as_done (task_list):
    view_task (task_list)
    try: 
        task_number = int (input("Enter the task number to mark as done"))
        task_list.pop (task_number - 1)
    except (ValueError, IndexError):
        print ("Invalid input, Please enter a valid task number:)")

def save_task (task_list):
    with open ("task.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")

def load_task (task_list):
    pass

isRunning = True

while isRunning == True:
    print ("1. Add Task")
    print ("2. View Task")
    print ("3. Mark Task as Done")
    print ("4. Exit the App\n")

    choose = int(input("Choose an option: "))

    if (choose == 1):
        task = input("Enter a task: ")
        add_task(task, task_list)
            
        addMore = False
        choice = input("Would you like to input more? [y/n]: ")
            
        if choice.lower() == 'Y':
            addMore = True
                
            task = input("Enter a task: ")
            add_task(task, task_list)

