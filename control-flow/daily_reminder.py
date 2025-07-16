# Ask the user to enter a task
task = input("Enter your task: ")

# Ask for the task priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Check if the task is time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority != "high":  # Only add this line if not already emphasized
        message += ". Consider completing it when you have free time."

# Print the final reminder
print("\n" + message)
