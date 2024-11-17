lista = [1, 2, 3, 4, 5]

def calculate_standard_deviation(lista:list) -> float:
    mean = sum(lista) / len(lista)
    lista_quadrado: list = []
    for i in lista:
        lista_quadrado.append((i - mean)**2)
    mean_quadrado = sum(lista_quadrado) / len(lista_quadrado)
    result = mean_quadrado**0.5
    return print(result)

calculate_standard_deviation(lista)