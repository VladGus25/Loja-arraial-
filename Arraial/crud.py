from dados import produtos, ids_cadastrados
from utils import validar_numero


def cadastrar_produto():

    id_produto = validar_numero("ID: ")

    if id_produto <= 0:
        print("ID inválido!")
        return

    if id_produto in ids_cadastrados:
        print("ID já cadastrado!")
        return

    nome = input("Nome do produto: ")

    if nome == "":
        print("Nome inválido!")
        return

    while True:

        try:
            preco = float(input("Preço: "))

            if preco < 0:
                print("Preço inválido!")
                continue

            break

        except ValueError:

            # BUG ENCONTRADO:
            # O sistema quebrava quando o usuário digitava letras.
            # Corrigido usando try/except.

            print("Digite um preço válido!")

    quantidade = validar_numero("Quantidade: ")

    if quantidade < 0:
        print("Quantidade inválida!")
        return

    produto = {
        "id": id_produto,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    ids_cadastrados.add(id_produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos():

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n===== PRODUTOS =====")

    print(
        f"{'ID':<5}"
        f"{'NOME':<20}"
        f"{'PREÇO':<10}"
        f"{'QTD':<5}"
    )

    for produto in produtos:

        nome_curto = produto["nome"][:20]

        print(
            f"{produto['id']:<5}"
            f"{nome_curto:<20}"
            f"{produto['preco']:<10}"
            f"{produto['quantidade']:<5}"
        )


def buscar_produto():

    id_busca = validar_numero("Digite o ID: ")

    for produto in produtos:

        if produto["id"] == id_busca:

            print("\nProduto encontrado!")

            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")

            return produto

    print("Produto não encontrado.")


def editar_produto():

    id_busca = validar_numero(
        "Digite o ID do produto: "
    )

    for produto in produtos:

        if produto["id"] == id_busca:

            print("Produto encontrado!")

            novo_nome = input("Novo nome: ")

            if novo_nome == "":
                print("Nome inválido!")
                return

            while True:

                try:

                    novo_preco = float(
                        input("Novo preço: ")
                    )

                    if novo_preco < 0:
                        print("Preço inválido!")
                        continue

                    break

                except ValueError:
                    print(
                        "Digite um preço válido!"
                    )

            nova_quantidade = validar_numero(
                "Nova quantidade: "
            )

            if nova_quantidade < 0:
                print("Quantidade inválida!")
                return

            produto["nome"] = novo_nome
            produto["preco"] = novo_preco
            produto["quantidade"] = nova_quantidade

            print("Produto atualizado!")

            return

    print("Produto não encontrado.")


def excluir_produto():

    id_busca = validar_numero("Digite o ID: ")

    for produto in produtos:

        if produto["id"] == id_busca:

            confirmar = input(
                "Deseja excluir? (s/n): "
            )

            if confirmar.lower() == "s":

                produtos.remove(produto)

                ids_cadastrados.remove(id_busca)

                print("Produto removido!")

            else:
                print("Exclusão cancelada.")

            return

    print("Produto não encontrado.")


def relatorio_estoque_baixo():

    estoque_baixo = [

        produto

        for produto in produtos

        if produto["quantidade"] < 5
    ]

    if not estoque_baixo:
        print("Nenhum produto com estoque baixo.")
        return

    print("\nProdutos com estoque baixo:")

    for produto in estoque_baixo:

        print(
            f"{produto['nome']} "
            f"- Quantidade: {produto['quantidade']}"
        )


def relatorio_quantidades():
    
    relatorio = {

        produto["nome"]: produto["quantidade"]

        for produto in produtos
    }

    print("\nRELATÓRIO:")

    for nome, quantidade in relatorio.items():

        print(f"{nome}: {quantidade}")