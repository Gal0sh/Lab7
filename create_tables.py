import psycopg2

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="shop", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

# Створення таблиць
cursor.execute("""
    CREATE TABLE Warehouses (
        warehouse_id SERIAL PRIMARY KEY,
        warehouse_name VARCHAR(255),
        manager_name VARCHAR(255),
        phone VARCHAR(50)
    );

    CREATE TABLE Products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255),
        category VARCHAR(50),
        price DECIMAL,
        stock INT
    );

    CREATE TABLE Clients (
        client_id SERIAL PRIMARY KEY,
        client_name VARCHAR(255),
        address TEXT,
        contact_person VARCHAR(255),
        phone VARCHAR(50)
    );

    CREATE TABLE Sales (
        sale_id SERIAL PRIMARY KEY,
        client_id INT REFERENCES Clients(client_id),
        product_id INT REFERENCES Products(product_id),
        quantity INT,
        sale_date DATE
    );
""")

conn.commit()
cursor.close()
conn.close()
print("Таблиці успішно створені.")
