
filename="tasks.txt"

def load_task():
  try: 
    with open(filename, "r") as f:
      for i in f:
        i=i.strip()
        if i:
          tasks.append(i)
  except FileNotFoundError:
    open(filename, "w").close()

def save_task():
  with open(filename, "w") as f :
      for i in tasks:
        f.write(i+"\n")

def add_task():
  task = input("Enter a new task: ").strip()
  if not task:
    print("Task cannot be empty")
    return
  tasks.append(task)
  save_task()
  print(f"Task '{task}' added")

def show_task():
  if not tasks:
    print("No task in the list! ")
  else:
    task_count=1
    for i in tasks:
      print(task_count,i)
      task_count=task_count+1

def remove_task():
  if not tasks:
    print("no tasks to remove!")
    return
  show_task()
  try:
    task_num=int(input("enter the task number to remove: "))
    if task_num in range(1,len(tasks)+1):
      removed_task=tasks.pop(task_num-1)
      print(f"TASK {removed_task} removed")
    else:
      print("enter a valid task number: ")
  except ValueError:
    print("enter a valid choice")


def mark_task_complete():
  if not tasks:
    print("no tasks to mark!")
    return
  show_task()
  try:
    task_num=int(input("enter the task number you completed: "))
    if task_num in range(1,len(tasks)+1):
      tasks[task_num-1]=tasks[task_num-1]+" ✅"
    else:
      print("please enter a valid task number")
  except ValueError:
    print("enter a valid choice")

print("To-do list options")
print("1. Show Tasks ")
print("2. Add Tasks")
print("3. Remove Task ")
print("4. Mark Task as completed ")
print("5. Exit")
load_task()

while True:
  try:
    task_num=int(input("choose an option: "))
    if task_num==1:
      show_task()
      print()
    elif task_num==2:
      add_task()
      print()
    elif task_num==3:
      remove_task()
      print()
    elif task_num==4:
      mark_task_complete()
      print()
    elif task_num==5:
      print("Bye 😔")
      break
    else:
      print("please enter a valid option")
      print()
  except ValueError :
    print("yikes thats a number")
