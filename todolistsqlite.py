import datetime
import sqlite3

DB_PATH = 'todolistsqllite/todolist.db'

# make database and return connection object
def make_db():
    connection = sqlite3.connect(DB_PATH)
    cur = connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS task(task TEXT, current_time TEXT, execution_time TEXT)""")
    return connection

# get current time in required format
def getting_current_time():
    current_time_func = datetime.datetime.now()
    current_time = current_time_func.strftime('%H:%M %Y-%m-%d')
    return current_time

# select all records from the database
def select_records(connection):
    cur = connection.cursor()
    cur.execute("""SELECT * FROM task""")
    result = cur.fetchall()
    for row in result:
        print(f'\nZadanie: {row[0]}\nData wyslania zadania: {row[1]}\nData wykonania zadania: {row[2]}\n')

# insert values into the database
def inserting_values(connection, current_time):
    task = input('Jakie zadanie chcesz dodac? ')
    execution_time = input('Kiedy ma zostać zrealizowane (od której do której) (format: 16:39-18:00 2023-3-21): ')
    cur = connection.cursor()
    cur.execute("""INSERT INTO task(task, current_time, execution_time) VALUES(?, ?, ?)""",(task, current_time, execution_time,))
    connection.commit()

# delete row from the database
def delete_row(connection):
    user_answer = int(input('\nJakiego zadania chcesz sie pozbyc? '))
    cur = connection.cursor()
    cur.execute(f"""DELETE FROM task WHERE rowid == {user_answer}""")

#executive program
while True:
    try:
        print('\n1. Pokaz zadania')
        print('2. Dodaj zadanie')
        print('3. Usun zadanie')
        print('4. Opusc program')
        option = int(input('Wybierz opcje: '))
        if option == 1:
            select_records(connection)
        elif option == 2:
            current_time = getting_current_time()
            inserting_values(connection, current_time)
        elif option == 3:
            delete_row(connection)
        elif option == 4:
            break
    except ValueError:
        print('Bledna opcja\n')
        
