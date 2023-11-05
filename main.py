from connect import connect
from create_db import create_db, create_table_users, create_table_messages, delete_table, delete_db


def app():
    OPCJE = """
    1 - stwórz baze danych
    2 - stwórz tabele users
    3 - stwórz tabele messages
    4 - usuń base danych
    5 - usuń tabele
    """


    connection = connect()
    cursor = connection.cursor()

    while True:
        opcja = input(OPCJE)
        print("twoja wybrana opcja to ", opcja)
        if opcja == '1':
            create_db(cursor)
            cursor.close()
        elif opcja == '2':
            create_table_users(cursor)

        elif opcja == '4':
            name = 'users_app'
            delete_db(name, cursor)

        elif opcja == '5':
            user = 'users'
            delete_table(user, cursor)
        elif opcja == '6':
            cursor.close()
            connection.close()
            break






if __name__ == "__main__":
    app()