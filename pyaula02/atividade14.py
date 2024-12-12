def remover_duplicatas(lista):
    
    return list(set(lista))


lista_original = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]


lista_sem_duplicatas = remover_duplicatas(lista_original)


print(f"Lista original: {lista_original}")
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")
