#Add tasks to a list
#Mark tasks as complete
#View tasks
#Quit

def add_task():
  task= input("Enter a task: ")
  task_info= {"task": task, "complete": False}
  tasks.append(task_info)
  print("Task added to the list successfully")

def mark_task_complete():
  incomplete_tasks= [task for task in tasks if task["complete"] == False]
  
  if len(incomplete_tasks) == 0:
    print("No tasks to mark as complete")
    return
    
  for i, task in enumerate(incomplete_tasks):
    print(f"{i+1}. {task['task']}")
    print("-" *30)
    
  task_number= int(input("Enter the number of the task to mark as complete: "))
  incomplete_tasks[task_number-1]["complete"]= True
  print("Task marked as complete")

def view_tasks():
  if not tasks :
    print("No tasks to view")
    return

  for i, task in enumerate(tasks):
    
    status= "✔" if task["complete"] else "❌"
    print(f"{i+1}. {task['task']} {status} ")
    print("-" *30)
    

message= """1.Add tasks to a list
2.Mark tasks as complete
3.View tasks
4.Quit"""

tasks=[]

while True:
  print(message)
  choice=input("Enter your choice:")
  if choice=="1":
    add_task()
  elif choice=="2":
    mark_task_complete()
  elif choice=="3":
    view_tasks()  
  elif choice=="4":
    break
  else:
    print("Invalid choice,please enter a number between 1  and 4")
  
  
