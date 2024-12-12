def uniao_conjuntos(*conjuntos):

    conjunto_resultante = set()
    for c in conjuntos:
        conjunto_resultante |= c  
    return conjunto_resultante


conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto3 = {5, 6, 7}


resultado = uniao_conjuntos(conjunto1, conjunto2, conjunto3)

# Exibindo o conjunto resultante
print(f"Conjunto resultante da união: {resultado}")
