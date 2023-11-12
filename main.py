import psycopg2
from psycopg2.errors import DuplicateDatabase, DuplicateTable, OperationalError
from connect import connect, connect_second
from create_db import create_db, create_table_users, create_table_messages, delete_table, delete_db
from models import User

def app():
    OPCJE = """
    1 - Create user
    2 - Find user by ID
    3 - Find user by Username
    4 - Find all users
    6 - Exit
    """


    connection = connect()
    cursor = connection.cursor()

    create_db(cursor)

    connection_second = connect_second()
    cursor_second = connection_second.cursor()

    create_table_users(cursor_second)
    create_table_messages(cursor_second)

    while True:
        opcja = input(OPCJE)
        print("Your selected option is \n", opcja)
        if opcja == '1':
            username = input('Username \n')
            user_password = input('User password \n')
            user = User(username, user_password)
            User.save_to_db(user, cursor_second)

        elif opcja == '2':
            id_user = input('ID user \n')
            print(User.load_user_by_id(cursor_second, id_user))

        elif opcja == '3':
            user_name = input('Enter name \n')
            print(User.load_user_by_username(cursor_second, user_name))

        elif opcja == '4':
            print(User.load_all_users(cursor_second))


        elif opcja == '6':
            cursor.close()
            connection.close()
            break





        # try:
        #     connection_second = connect_second()
        #     cursor_second = connection_second.cursor()
        #     create_table_users(cursor_second)
        # except psycopg2.DuplicateTable:
        #     print("The table exists")
        # try:
        #     create_table_messages(cursor_second)
        # except psycopg2.DuplicateTable:
        #     print("The table exists")

    cursor.close()
    connection.close()
    cursor_second.close()
    connection_second.close()














if __name__ == "__main__":
    app()