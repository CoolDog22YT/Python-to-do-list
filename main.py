import datetime
to_do_list_name = input("Please enter the name of your to-do list: ")
to_do_list = input("Enter a task for your to-do list: ")
to_do_list_date = input("When should it be done? (Format: YYYY-MM-DD) ")
print(f"Task '{to_do_list}' due on {to_do_list_date} has been added to '{to_do_list_name}' to-do list.")

if input("Has the task been completed? (yes/no): ") == "yes":
    print("Great job!")
else:
    print("You can do it!")

if to_do_list_date < datetime.date.today().strftime("%Y-%m-%d"):
    print("Warning: Task is past due!")

