def adicionar_ou_atualizar(dicionario, chave, valor):
    dicionario[chave] = valor  
    return dicionario


dicionario = {
    "Nome": "Joelson",
    "Idade": 29
}


chave = input("Digite a chave: ")
valor = input("Digite o valor: ")


if valor.isdigit():
    valor = int(valor)


dicionario = adicionar_ou_atualizar(dicionario, chave, valor)


print("Dicionário atualizado:", dicionario)
