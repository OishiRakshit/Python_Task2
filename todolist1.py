while True:
    print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Choose: ")

    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f]
    except:
        tasks = []

    if choice == "1":
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")
    
    elif choice == "2":
        task = input("Enter task: ")
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            num = int(input("Task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                with open("tasks.txt", "w") as f:
                    for task in tasks:
                        f.write(task + "\n")
            else:
                print("Invalid number.")
        except:
            print("Enter a valid number.")
    
    elif choice == "4":
        break

    else:
        print("Invalid choice.")

