def contar_ate_vinte():
    for i in range(20):
        print(i)

contar_ate_vinte()

def conte_usuario():
    contagem_usuario = int(input("Digite um número para poder fazer a contagem: "))

    for i in range(1, contagem_usuario):
        print(i)
conte_usuario()

def tabuada_2():

    i = 1
    print(f"Tabuada de: 2")
    while i <= 10:
        soma = 2 + i
        print(f"{2} + {i} = {soma}")
        i += 1
tabuada_2()

def tabuada_usuario():
    i = 1
    digito = int(input("Digite um número inteiro para imprimir a tabuada: "))
    print("A tabuada do número é:")
    while i <= 10:
        soma = digito * i
        print(f"{digito} * {i} = {soma}")
        i += 1

tabuada_usuario()