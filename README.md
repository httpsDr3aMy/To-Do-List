#To-do List Manager with SQLite Database
This is a Python program that allows you to manage your to-do list using an SQLite database. The program provides the following functionality:

- Show tasks in the database
- Add a task to the database
- Remove a task from the database
- Exit the program

#Prerequisites
Python 3.x
SQLite3

#Setup
1. Clone the repository
2. Navigate to the cloned directory
3. Run the program with python3 main.py

#Functions
make_db()
This function creates a connection to an SQLite database named 'todolist.db' and creates a table named 'task' with columns 'task', 'current_time', and 'execution_time' if the table does not already exist.

getting_current_time()
This function gets the current date and time and returns it as a string in the format "hour:minute year-month-day".

select_records(connection)
This function selects all rows from the 'task' table in the connected database and prints them to the console.

inserting_values(connection, current_time)
This function prompts the user to enter a task and the execution time for the task, then inserts the values into the 'task' table in the connected database.

delete_row(connection)
This function prompts the user to enter the row number of the task they want to delete, then deletes that row from the 'task' table in the connected database.

#Usage
1. Run the program with python3 main.py
2. Choose an option from the menu:
  1. Show tasks
  2. Add task
  3. Remove task
  4. Exit program
3. Follow the prompts to add or remove tasks
4. Tasks and their execution times are stored in the database for future reference.

#Limitations
The program does not handle errors or exceptions gracefully, so it may crash or behave unexpectedly if incorrect input is provided.
The execution time for tasks is stored as a string in a specific format, so the user must input the time in the correct format for it to be stored correctly.
The program only allows the user to remove tasks by their row number, so if a task is added or removed, the row numbers of the other tasks may change.
