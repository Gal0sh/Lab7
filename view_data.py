import psycopg2

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="shop", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

# Таблиці для виведення
tables = ["Warehouses", "Products", "Clients", "Sales"]

for table in tables:
    print(f"Таблиця: {table}")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("-" * 50)

conn.close()
