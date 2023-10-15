import datetime
from database import create_table, insert_product, list_materials, is_product_registered
from orders import insert_order, list_orders, update_order_status, can_produce


def get_available_quantity(product_name):
    materials = list_materials()
    for material in materials:
        name, quantity = material
        if name == product_name:
            return quantity
    return 0


def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main_menu():
    while True:
        print("Opções:")
        print("1. Registrar uma nova ordem de produção")
        print("2. Listar todas as ordens de produção")
        print("3. Atualizar o status de uma ordem de produção")
        print("4. Listar produtos cadastrados")
        print("5. Cadastrar um novo produto")
        print("6. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            while True:
                product_name = input("Nome do produto (ou 'exit' para cancelar): ")
                if product_name.lower() == "exit":
                    break  # Sair do loop interno
                if not is_product_registered(product_name):
                    print("Produto não cadastrado.")
                    continue  # Volta ao início do loop interno

                available_quantity = get_available_quantity(product_name)

                while True:
                    quantity_input = input(
                        "Quantidade desejada (ou 'exit' para cancelar): "
                    )
                    if quantity_input.lower() == "exit":
                        break  # Sair do loop interno
                    try:
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("A quantidade deve ser maior que zero.")
                        elif quantity <= available_quantity:
                            result = can_produce(product_name, quantity)
                            if result is True:
                                break
                            else:
                                print(result)
                        else:
                            print("Quantidade desejada maior que a disponível.")
                    except ValueError:
                        print(
                            "Quantidade inválida. Digite 'exit' para cancelar o cadastro."
                        )

                if quantity_input.lower() == "exit":
                    break  # Sair do loop interno

                while True:
                    delivery_date = input(
                        "Data de entrega (AAAA-MM-DD) (ou 'exit' para cancelar): "
                    )
                    if delivery_date.lower() == "exit":
                        break  # Sair do loop interno
                    if is_valid_date(delivery_date):
                        current_date = datetime.date.today()
                        delivery_date = datetime.datetime.strptime(
                            delivery_date, "%Y-%m-%d"
                        ).date()

                        if delivery_date > current_date:
                            result = can_produce(product_name, quantity)

                            if result is True:
                                insert_order(product_name, quantity, delivery_date)
                                print("Ordem de produção registrada com sucesso!")
                                break  # Sair do loop interno
                            else:
                                print(f"Não é possível produzir devido a: {result}")
                        else:
                            print("A data de entrega deve ser maior que a data atual.")
                    else:
                        print("Data de entrega inválida. Use o formato AAAA-MM-DD.")

        elif choice == "2":
            orders = list_orders()
            print("Ordens de produção:")
            if not orders:
                print("Nenhuma ordem de produção encontrada.")
            else:
                for order in orders:
                    order_id, product_name, quantity, delivery_date, status = order
                    formatted_order = f"ID Pedido: {order_id}, Produto: {product_name}, Quantidade: {quantity}, Data de Entrega: {delivery_date}, Status: {status}"
                    print(formatted_order)

        elif choice == "3":
            order_id = int(input("ID da ordem de produção: "))
            new_status = input("Novo status (Concluída ou Em andamento): ")
            update_order_status(order_id, new_status)
            print("Status atualizado com sucesso!")

        elif choice == "4":
            materials = list_materials()
            print("Produtos cadastrados:")
            if not materials:
                print("Nenhum produto cadastrado.")
            else:
                for material in materials:
                    product, quantity = material
                    formatted_material = (
                        f"Produto: {product}, Quantidade em Estoque: {quantity}"
                    )
                    print(formatted_material)

        elif choice == "5":
            product_name = input("Nome do novo produto: ")
            quantity = int(input("Quantidade em estoque: "))
            insert_product(product_name, quantity)
            print("Produto cadastrado com sucesso!")

        elif choice == "6":
            break


if __name__ == "__main__":
    create_table()
    main_menu()
