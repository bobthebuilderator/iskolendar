#Declaration of lists, class, and other variables
#Class of Teacher Accounts (Username: Password)
teacher_accounts = {"teacher": "teacher123"}

#Class of Student Accounts (Username: Password)
student_accounts = {"student": "student123"}

#Default List of Students
students = ["Nicko", "Gen", "Nemo", "Bea", "Rover"]

#Other Lists
tasks = []
events = []
schedules = []

#User-Defined Funtions used in the Program

#User-Defined Log-in Function
def login():
    
    #Log-in Menu
    log_in_option = input(f"""
===== Log-In =====
Enter the number of your chosen option:
1. Teacher
2. Student

Or press any key to exit.""")

    #Teacher Log-in
    if log_in_option == "1":
        #User-input
        username = input("Username: ")
        password = input("Password: ")

        #Condition for Successful Log-in
        if username in teacher_accounts and teacher_accounts[username] == password:
            print("Login successful\n")
            teacher_menu()
            return True

        #Insuccessful Log-in
        else:
            print("Invalid login\n")
            return False

    #Student Log-in
    elif log_in_option == "2":
        #User-input
        username = input("Username: ")
        password = input("Password: ")

        #Condition for Successful Log-in
        if username in student_accounts and student_accounts[username] == password:
            print("Login successful\n")
            student_menu()
            return True

        #Unsuccessful Log-in
        else:
            print("Invalid login\n")
            return False
    #User didn't choose to Log-in
    else:
        print("Thank you!")
        return False

#User-Defined Add Task Name Function 
def add_item(item_type, storage):

    #User-input
    name = input(f"{item_type} name: ")
    date = input("Date (YYYY-MM-DD): ")

    #Stores the date and name the task is scheduled for
    storage.append((date, name))

    #User-confirmatio
    print(f"{item_type} added\n")

#User-Defined View Calendar Function
def view_calendar():

    print("\n===== CALENDAR =====")

    for date, name in tasks:
        print(f"{date} - Task: {name}")

    for date, name in events:
        print(f"{date} - Event: {name}")

    for date, name in schedules:
        print(f"{date} - Schedule: {name}")

    print()

#User-Defined Function for Menu for Teachers
def teacher_menu():
    
    #Loop of Main Menu for Teachers
    while True:
        choice = input("""===== MENU =====
    1. View Students
    2. Add Task
    3. Add Event
    4. Add Schedule
    5. View Calendar

    Or press any key to exit.
    
    Choose: """)

        #View Student List
        if choice == "1":

            print("\nStudents:")
            for s in students:
                print("-", s)
            print()

        #Add Tasks
        elif choice == "2":
            add_item("Task", tasks)

        #Add Events
        elif choice == "3":
            add_item("Event", events)

        #Add Schedule
        elif choice == "4":
            add_item("Schedule", schedules)

        #View Calendar
        elif choice == "5":
            view_calendar()

        #Log-out
        else:
            print("Logging out\n")
            break

#User-Defined Function for Menu for students
def student_menu():
    
    #Loop of Main Menu for Students
    while True: 
        choice = input("""===== MENU =====
    1. Add Task
    2. Add Event
    3. Add Schedule
    4. View Calendar

    Or press any key to exit.
    
    Choose: """)

        #Add Tasks
        if choice == "1":
            add_item("Task", tasks)

        #Add Events
        elif choice == "2":
            add_item("Event", events)

        #Add Schedule
        elif choice == "3":
            add_item("Schedule", schedules)

        #View Calendar
        elif choice == "4":
            view_calendar()

        #Log-out
        else:
            print("Logging out\n")
            break

#Start of Working Program
while True:

    print("===== Welcome to the Menu =====")

    if login():
        status = "yes"
    else:
        break
