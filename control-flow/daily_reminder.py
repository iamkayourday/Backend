# Personal Daily Reminder

task = input("Enter your task: ")
Priority =  input("Proirity (high/medium/low): ") 
time_bound = input("Is it time-bound? (yes/no): ")


match Priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is high priority that requires immediate attention today")
        elif time_bound == "no":
            print(f"{task} is high priority task, but is not time bound. Consider completing it when you have free time")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is medium priority that requires attention today, but can be done after high priority tasks")
        elif time_bound == "no":
            print(f"{task} is medium priority task that can be completed at your convenience")
    case "low":
        if time_bound == "yes":
            print(f"{task} is low priority that can be done today if time allows")
        elif time_bound == "no":
            print(f"{task} is low priority task that can be completed whenever you have time")

# Didn't believe I could do this!!!