import psycopg2

def get_db_connection(params):
    return psycopg2.connect(**params)
