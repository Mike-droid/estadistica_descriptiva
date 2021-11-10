import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

def calcula_mediana(valores):
    valores.sort()
    if len(valores) % 2 == 0:
        return (valores[len(valores) // 2] + valores[len(valores) // 2 - 1]) / 2
    else:
        return valores[len(valores) // 2]

print(f'La mediana de {sorted(random_numbers)} es {calcula_mediana(random_numbers)}')