from database import products, categories

def add_product(product_id, name, category_id):
    """Adiciona um novo produto."""
    if product_id in products:
        print(f"Produto com id {product_id} já existe.")
    elif category_id not in categories:
        print(f"Categoria com id {category_id} não existe.")
    else:
        products[product_id] = {'name': name, 'category_id': category_id}
        print(f"Produto '{name}' adicionado com sucesso.")

def update_product(product_id, new_name, new_category_id):
    """Atualiza um produto existente."""
    if product_id not in products:
        print(f"Produto com id {product_id} não encontrado.")
    elif new_category_id not in categories:
        print(f"Categoria com id {new_category_id} não existe.")
    else:
        products[product_id] = {'name': new_name, 'category_id': new_category_id}
        print(f"Produto id {product_id} atualizado com sucesso.")

def delete_product(product_id):
    """Apaga um produto."""
    if product_id in products:
        del products[product_id]
        print(f"Produto id {product_id} deletado com sucesso.")
    else:
        print(f"Produto com id {product_id} não encontrado.")

def list_products():
    """Lista todos os produtos."""
    if products:
        for id, info in products.items():
            category_name = categories.get(info['category_id'], "Categoria não encontrada")
            print(f"ID: {id}, Nome: {info['name']}, Categoria: {category_name}")
    else:
        print("Não há produtos cadastrados.")

def list_products_by_category(category_id):
    """Lista produtos de uma categoria específica."""
    if category_id not in categories:
        print(f"Categoria com id {category_id} não encontrada.")
        return

    found = False
    for id, info in products.items():
        if info['category_id'] == category_id:
            print(f"ID: {id}, Nome: {info['name']}")
            found = True
    if not found:
        print("Não foram encontrados produtos nesta categoria.")

def add_category(category_id, name):
    """Adiciona uma nova categoria."""
    if category_id in categories:
        print(f"Categoria com id {category_id} já existe.")
    else:
        categories[category_id] = name
        print(f"Categoria '{name}' adicionada com sucesso.")

def update_category(category_id, new_name):
    """Atualiza o nome de uma categoria existente."""
    if category_id in categories:
        categories[category_id] = new_name
        print(f"Categoria id {category_id} atualizada para '{new_name}'.")
    else:
        print(f"Categoria com id {category_id} não encontrada.")

def delete_category(categories, category_id):
    """Deleta uma categoria existente."""
    if category_id in categories:
        del categories[category_id]
        return True, "Categoria deletada com sucesso."
    else:
        return False, "Categoria não encontrada."

def list_categories():
    """Lista todas as categorias."""
    if categories:
        for id, name in categories.items():
            print(f"ID: {id}, Nome: {name}")
    else:
        print("Não há categorias cadastradas.")