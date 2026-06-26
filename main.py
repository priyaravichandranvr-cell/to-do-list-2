# To-Do List Program

tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        t = input("Enter task: ")
        tasks.append(t)
        print("Task added!")

    elif choice == "2":
        if tasks == []:
            print("No tasks yet")
        else:
            print("Tasks are:")
            i = 1
            for t in tasks:
                print(i, "-", t)
                i = i + 1

    elif choice == "3":
        if tasks == []:
            print("Nothing to delete")
        else:
            print("Select task number to delete:")
            i = 1
            for t in tasks:
                print(i, "-", t)
                i += 1

            num = int(input("Enter number: "))
            if num >= 1 and num <= len(tasks):
                print("Deleted:", tasks[num-1])
                tasks.pop(num-1)
            else:
                print("Wrong number")

    elif choice == "4":
        print("Program ended")
        break

    else:
        print("Invalid input")