def imprimi_nomes():
    nomes = ['Joao', 'Maria', 'Fulano', 'Siclano']

    print("1 -", nomes[0])
    print("2 -", nomes[1])
    print("3 -", nomes[2])
    print("4 -", nomes[3])

imprimi_nomes()

def imprimi_ultimo_nome():
    nomes = ['Joao', 'Maria', 'Fulano', 'Siclano']

    print("Ultimo nome:", nomes[3])

imprimi_ultimo_nome()

def troca_nome_lista():

    lista_mercado = ["Macarrão", "Pepino", "Batata"]

    print("Está é a sua lista atual:", lista_mercado)
    print("Digite o nome do item que deseja trocar:")

    novo_item1 = str(input("1: "))
    novo_item2 = str(input("2: "))
    novo_item3 = str(input("3: "))

    lista_mercado[0] = novo_item1
    lista_mercado[1] = novo_item2
    lista_mercado[2] = novo_item3

    print("Nova lista do mercado:")
    print("1 -", lista_mercado[0])
    print("2 -", lista_mercado[1])
    print("3 -", lista_mercado[2])

troca_nome_lista()