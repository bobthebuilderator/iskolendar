# GROUP PENT-A-GON’S DOCUMENTATION FILE
------
1. **Logic Plan**


{content: START
 Display welcome message

 call login()
  Display Log-in Options (teacher/student/exit)
  IF Teacher:
    Input Teacher Credentials
    IF Valid: goto teacher_menu()
  IF Student:
    Input Student Credentials
    IF Valid: goto student_menu()
  ELSE: Exit

IF login() == True: Loop Back to Start
ELSE: End

teacher_menu():
 Display Menu Options (View Students/Add Task, Event, or Schedule/View Calendar/Exit)
 Perform action based on choice
 Loop Back to Menu

student_menu():
 Display Menu Options (Add Task, Event,or Schedule/View Calendar/Exit)
 Loop Back to Menu
Perform action based on choice}

2. **System Explanation**

	Our program features a log-in system that prompts users to choose whether they want to log in or not, as either a teacher or a student. Once logged in, depending on whether the user is a teacher or a student, a different menu is displayed for each. For teachers, they can choose to view the default list of students, add tasks, events, and schedules, and also view the calendar. For students, they have the same options, except they can’t view the default list of students. The user can exit the program anytime, breaking the program’s loop.

3. **Limitations and Future Improvements**

	The program has limited options in the main menu for both teachers and students. Based on the program’s planned features, so far it lacks the ability to organize tasks, which is the purpose of the Iskolendar. Additional features that could be added in the future for the teacher’s dashboard/menu on the calendar include: Adding descriptions and information to a task/event/schedule (type, place, due date, etc.), differentiating between schedules, and the option to check the student list and the status of their assessments (complete/incomplete). For the students, additional options that could be added in the future are: the choice to view the official/default school calendar and change the status of their assessments. Future improvements in the code include better code readability, efficiency and organization.

