import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"F:\Thesis\web-flask\database.db"

    sql_create_broker_table = """CREATE TABLE IF NOT EXISTS [broker] (
                                        [id_device] integer NOT NULL PRIMARY KEY,
                                        [ip_device] varchar(32),
                                        [uptime_at] timestamp default current_timestamp NOT NULL,
                                        [location] varchar(32)
                                    );"""
    sql_create_device_table = """CREATE TABLE IF NOT EXISTS [device] (
                                        FOREIGN KEY (id_device) REFERENCES broker (id_device),
                                        [name] varchar[32],
                                        [value] real,
                                        [state] boolean
                                    );"""

    conn = create_connection(database)

    if conn:
        create_table(conn, sql_create_broker_table)
        create_table(conn, sql_create_device_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
