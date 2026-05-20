tasks = []

while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == 3:
        task = input("Enter task to remove: ")

        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")