import psycopg2
from faker import Faker
import random

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="shop", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

faker = Faker()

# Заповнення таблиці "Warehouses"
for _ in range(3):
    cursor.execute(
        "INSERT INTO Warehouses (warehouse_name, manager_name, phone) VALUES (%s, %s, %s)",
        (faker.company(), faker.name(), faker.phone_number())
    )

# Заповнення таблиці "Products"
for _ in range(17):
    cursor.execute(
        "INSERT INTO Products (product_name, category, price, stock) VALUES (%s, %s, %s, %s)",
        (
            faker.word(),
            random.choice(["Чоловічий", "Жіночий", "Дитячий"]),
            round(random.uniform(100, 1000), 2),
            random.randint(1, 50)
        )
    )

# Заповнення таблиці "Clients"
for _ in range(7):
    cursor.execute(
        "INSERT INTO Clients (client_name, address, contact_person, phone) VALUES (%s, %s, %s, %s)",
        (faker.name(), faker.address(), faker.name(), faker.phone_number())
    )

# Заповнення таблиці "Sales"
for _ in range(22):
    cursor.execute(
        "INSERT INTO Sales (client_id, product_id, quantity, sale_date) VALUES (%s, %s, %s, %s)",
        (
            random.randint(1, 7),
            random.randint(1, 17),
            random.randint(1, 5),
            faker.date_this_year()
        )
    )

conn.commit()
cursor.close()
conn.close()
print("Дані успішно додано.")
