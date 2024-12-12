notas = {
    "João": 7.5,
    "Maria": 8.0,
    "Carlos": 6.5,
    "Ana": 9.0,
    "Pedro": 7.0
}

def calcular_media(notas):
    total = sum(notas.values())  
    quantidade = len(notas)  
    media = total / quantidade  
    return media


media = calcular_media(notas)
print(f"A média das notas é: {media:.2f}")
