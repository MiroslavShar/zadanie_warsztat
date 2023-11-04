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


