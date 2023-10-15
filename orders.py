from database import get_connection


def insert_order(product_name, quantity, delivery_date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO production_orders (product_name, quantity, delivery_date, status) "
        "VALUES (%s, %s, %s, %s)",
        (product_name, quantity, delivery_date, "Em andamento"),
    )
    connection.commit()
    cursor.close()
    connection.close()


def list_orders():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM production_orders")
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return orders


def update_order_status(order_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE production_orders " "SET status = %s " "WHERE id = %s",
        (status, order_id),
    )
    connection.commit()
    cursor.close()
    connection.close()


def can_produce(product_name, quantity):
    total_quantity_in_progress = sum(
        order[2]
        for order in list_orders()
        if order[1] == product_name and order[4] == "Em andamento"
    )
    available_quantity = get_available_quantity(product_name)
    if total_quantity_in_progress + quantity <= available_quantity:
        return True
    return f"Quantidade insuficiente. Disponível: {available_quantity}, em andamento: {total_quantity_in_progress}"


def get_available_quantity(product_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT quantity FROM materials WHERE product_name = %s", (product_name,)
    )
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] if result else 0
