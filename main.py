import datetime

import psycopg2
from psycopg2.errors import DuplicateDatabase, DuplicateTable, OperationalError
from connect import connect, connect_second
from create_db import create_db, create_table_users, create_table_messages, delete_table, delete_db
from models import User, Messages


def app():
    OPCJE = """
    1 - Create user
    2 - Find user by ID
    3 - Find user by Username
    4 - Find all users
    5 - Edit user
    6 - Delete user
    7 - Create message
    8 - Find all messages
    9 - Exit
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

        elif opcja == '5':
            id_user = input('ID user \n')
            print(User.load_user_by_id(cursor_second, id_user))
            new_username = input('Username \n')
            new_password = input('New password \n')
            User.edit_password(cursor_second, id_user, new_username, new_password)

        elif opcja == '6':
            username = input('Username \n')
            print(User.load_user_by_username(cursor_second, username))
            User.delete(User(username), cursor_second)

        elif opcja == '7':
            text = input('Write your message \n')
            from_id = input("Who will be sending \nInput ID user \n")
            to_id = input("Who will be the receiver \nInput ID user \n")
            message = Messages(from_id, to_id, text)
            Messages.save_to_db(message, cursor_second)

        elif opcja == '8':
            print(Messages.loaded_all_messages(cursor_second))


        elif opcja == '9':
            cursor.close()
            connection.close()
            break










    cursor.close()
    connection.close()
    cursor_second.close()
    connection_second.close()














if __name__ == "__main__":
    app()