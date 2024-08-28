todo=[]
completed=[]
def input() :
    task=input("enter  a task")
    todo.append(task)

def remove() :
    try:
        n = int(input("Enter the number of the task you want to delete: "))
        if 0 <= n < len(todo):
            todo.pop(n)
        else:
            print("Invalid task number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

def complete() :
    try:
        nm = int(input("Enter the number of the task you want to complete: "))
        if 0 <= nm < len(todo):
            completed.append(todo[nm])
            todo.pop(nm)
        else:
            print("Invalid task number.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
def display() :
    for i in range(len(todo)) :
        print(todo[i])

    for i in range(len(completed)) :
        print(completed[i])

while(True) :
   
    choice = input("insert,remove,complete,display,exit enter a choice same as above:::").strip().lower()
    if(choice=='insert') :
        input()
    elif choice=='remove' :
        remove()
    elif choice=='complete' :
        complete()
    elif choice=='display' :
        display()
    else :
        exit()

