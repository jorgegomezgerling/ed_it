import psycopg2

# Connect to your postgres DB

conn = psycopg2.connect(
    database="Curso",
    user="postgres",
    password="abcd",
    host="localhost",
    port='5433'
)

# con = psycopg2.connect()


# Open a cursor to perform database operations
cur = conn.cursor()

# # Execute a query
cur.execute("SELECT * FROM alumnos WHERE apellidomaterno='Perez'")

# # Retrieve query results
records = cur.fetchall()

for i in records:
    print(i)

conn.close()