votacao = {}


def exibir_opcoes():
    print("\nOpções de Votação:")
    for numero, opcao in enumerate(votacao.keys(), 1):
        print(f"{numero}. {opcao}")
    print("0. Encerrar votação")


def registrar_voto(opcao):
    if opcao in votacao:
        votacao[opcao] += 1
    else:
        print("Opção inválida! Tente novamente.")


def mostrar_resultados():
    print("\nResultados Finais:")
    for opcao, votos in votacao.items():
        print(f"{opcao}: {votos} votos")

def sistema_votacao():
    while True:
        print("\nDigite o nome de uma nova opção de voto ou '0' para encerrar a votação.")
        nova_opcao = input("Opção: ")


        if nova_opcao == '0':
            break

        if nova_opcao not in votacao:
            votacao[nova_opcao] = 0

    while True:
        exibir_opcoes()
        try:
            escolha = int(input("Digite o número da opção que deseja votar ou '0' para encerrar: "))
            if escolha == 0:
                break
            opcoes_lista = list(votacao.keys())
            if 1 <= escolha <= len(opcoes_lista):
                registrar_voto(opcoes_lista[escolha - 1])
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    mostrar_resultados()

# Rodando o programa
sistema_votacao()
