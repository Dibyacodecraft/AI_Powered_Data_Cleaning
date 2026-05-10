import psycopg2
from psycopg2 import sql

DB_host = "localhost"
Port = 5432
DB_name = "demoDB"
Username = "postgres"
Password = "admin"
Table_name = "my_table"


def test_postgres_connection():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            database=DB_name,
            user=Username,
            password=Password,
            host=DB_host,
            port=Port,
        )
        cursor = connection.cursor()
        cursor.execute(sql.SQL("SELECT * FROM {} LIMIT 5").format(sql.Identifier(Table_name)))
        rows = cursor.fetchall()
        print("Postgres connection was successful")
        print("Rows from database:", rows)
    except Exception as exc:
        print(f"Error: {exc}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    test_postgres_connection()
