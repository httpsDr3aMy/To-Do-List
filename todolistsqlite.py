import datetime, sqlite3

#making database
def make_db():
    try:
        connection = sqlite3.connect('todolistsqllite/todolist.db')
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text, current_time text, execution_time text)""")
    except Exception:
        pass
    return connection

connection = make_db()

#getting current time to print date of giving task
def getting_current_time():
    current_time_func = datetime.datetime.now()
    day = current_time_func.day
    month = current_time_func.month
    year = current_time_func.year
    hour = current_time_func.hour
    minutes = current_time_func.minute
    current_time = str(hour)+':'+str(minutes)+' '+str(year)+'-'+str(month)+'-'+str(day)
    return current_time

#selecting all records
def select_records(connection):
    cur = connection.cursor()
    cur.execute("""SELECT * FROM task""")
    result = cur.fetchall()
    for row in result:
        print(
            f'\nZadanie: {str(row[0])}'
            + '\nData wyslania zadania: '
            + str(row[1])
            + '\nData wykonania zadania: '
            + str(row[2])
            + '\n'
        )

#inserting values to database
def inserting_values(connection, current_time):
    task = input('Jakie zadanie chcesz dodac? ')
    execution_time = input('Kiedy ma zostać zrealizowane (od której do której) (format: 16:39-18:00 2023-3-21): ')
    cur = connection.cursor()
    cur.execute("""INSERT INTO task(task, current_time, execution_time) VALUES(?, ?, ?)""",(task, current_time, execution_time,))
    connection.commit()

#deleting rows which user selected
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
        