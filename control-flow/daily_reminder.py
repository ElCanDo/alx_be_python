task = input("Task description: ")
priority = input("Priority (high,medium,low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Note: '{task}' is a high priority task.")

    case "medium":
        print(f"Note: '{task}' is a medium priority task.Consider completing it during your free time.")
    
    case "low":
        print(f"Note: '{task}' is a low priority task. You can complete it any time you wish to.")

if time_bound == "yes":
    print("Reminder: '{task}' This task requires immediate attention today!.")
    
