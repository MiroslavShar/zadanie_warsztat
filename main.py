from connect import connect
from create_db import create_db, create_table_users, create_table_messages


def app():
    OPCJE = """
    1 - stwórz baze danych
    2 - stwórz tabele users
    3 - stwórz tabele messages
    """


    connection = connect()
    cursor = connection.cursor()

    while True:
        opcja = input(OPCJE)
        print("twoja wybrana opcja to ", opcja)
        if opcja == '1':
            create_db(cursor)
        elif opcja == '2':
            create_table_users(cursor)
        elif opcja == '3':
            create_table_messages(cursor)



if __name__ == "__main__":
    app()