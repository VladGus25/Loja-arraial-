from dados import produtos

def gerador_produtos():

    for produto in produtos:
        yield produto


def validar_numero(mensagem):

    while True:

        try:
            valor = int(input(mensagem))
            return valor

        except ValueError:

            print("Digite um número válido!")