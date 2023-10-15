import mysql.connector

# Configurações de conexão ao banco de dados
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "senha_root",
    "database": "production_orders",
}

def create_table():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS production_orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255),
            quantity INT,
            delivery_date DATE,
            status VARCHAR(50)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS materials (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255),
            quantity INT
        )
        """
    )
    connection.commit()
    cursor.close()
    connection.close()

def get_connection():
    return mysql.connector.connect(**db_config)

def insert_product(product_name, quantity):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO materials (product_name, quantity) VALUES (%s, %s)",
        (product_name, quantity)
    )
    connection.commit()
    cursor.close()
    connection.close()

def is_product_registered(product_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM materials WHERE product_name = %s",
        (product_name,)
    )
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] > 0

def list_materials():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT product_name, quantity FROM materials")
    materials = cursor.fetchall()
    cursor.close()
    connection.close()
    return materials
