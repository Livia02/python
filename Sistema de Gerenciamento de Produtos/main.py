from lib.funcoes import add_category, update_category, delete_category, list_categories
from lib.funcoes import add_product, update_product, delete_product, list_products, list_products_by_category
from database import categories, products

def main_menu():
    print("\nSistema de Gerenciamento de Produtos")
    print("1. Gerenciar Categorias")
    print("2. Gerenciar Produtos")
    print("3. Sair")
    choice = input("Escolha uma opção: ")
    return choice

def category_menu():
    print("\nGerenciamento de Categorias")
    print("1. Adicionar Categoria")
    print("2. Atualizar Categoria")
    print("3. Deletar Categoria")
    print("4. Listar Categorias")
    print("5. Voltar")
    choice = input("Escolha uma opção: ")
    return choice

def product_menu():
    print("\nGerenciamento de Produtos")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Deletar Produto")
    print("4. Listar Todos os Produtos")
    print("5. Listar Produtos por Categoria")
    print("6. Voltar")
    choice = input("Escolha uma opção: ")
    return choice

def handle_categories():
    while True:
        choice = category_menu()
        if choice == "1":
            id = input("ID da Categoria: ")
            name = input("Nome da Categoria: ")
            print(add_category(categories, id, name)[1])
        elif choice == "2":
            id = input("ID da Categoria: ")
            new_name = input("Novo Nome da Categoria: ")
            print(update_category(categories, id, new_name)[1])
        elif choice == "3":
            id = input("ID da Categoria para deletar: ")
            print(delete_category(categories, id)[1])
        elif choice == "4":
            print(list_categories(categories))
        elif choice == "5":
            break
        else:
            print("Opção inválida.")

def handle_products():
    while True:
        choice = product_menu()
        if choice == "1":
            id = input("ID do Produto: ")
            name = input("Nome do Produto: ")
            category_id = input("ID da Categoria: ")
            print(add_product(products, id, name, category_id)[1])
        elif choice == "2":
            id = input("ID do Produto: ")
            new_name = input("Novo Nome do Produto: ")
            new_category_id = input("Novo ID da Categoria: ")
            print(update_product(products, id, new_name, new_category_id)[1])
        elif choice == "3":
            id = input("ID do Produto para deletar: ")
            print(delete_product(products, id)[1])
        elif choice == "4":
            print(list_products(products))
        elif choice == "5":
            category_id = input("ID da Categoria para listar produtos: ")
            print(list_products_by_category(products, category_id))
        elif choice == "6":
            break
        else:
            print("Opção inválida.")

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            handle_categories()
        elif choice == "2":
            handle_products()
        elif choice == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
