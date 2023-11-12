import psycopg2

settings = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'coderslab',
    'port': '5433'
}

def connect():
    connection = psycopg2.connect(**settings)
    connection.autocommit = True
    return connection


settings_new = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'coderslab',
    'database': 'users_app',
    'port': '5433'
}

def connect_second():
    connection_second = psycopg2.connect(**settings_new)
    connection_second.autocommit = True
    return connection_second


