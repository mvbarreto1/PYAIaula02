def verificar_chaves(dicionario, chaves):

    return all(chave in dicionario for chave in chaves)


dicionario = {
    "Nome": "Joelson",
    "Idade": 29,
    "Profissão": "Engenheiro"
}

chaves = ["Nome", "Idade", "Profissão"]


resultado = verificar_chaves(dicionario, chaves)


print("Todas as chaves existem no dicionário?", resultado)
