from crud import (
    cadastrar_produto,
    listar_produtos,
    buscar_produto,
    editar_produto,
    excluir_produto,
    relatorio_estoque_baixo,
    relatorio_quantidades
)

while True:

    print("\n===== ARRAIAL MODAS =====")

    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Editar Produto")
    print("5 - Excluir Produto")
    print("6 - Relatório Estoque Baixo")
    print("7 - Relatório Quantidades")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        editar_produto()

    elif opcao == "5":
        excluir_produto()

    elif opcao == "6":
        relatorio_estoque_baixo()

    elif opcao == "7":
        relatorio_quantidades()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")