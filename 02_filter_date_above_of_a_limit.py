
lista: list = [1, 2, 3, 4, 5]

def filter_values_above_4(list: list, limit: float) -> list[float]:
    result = []
    for i in list:
        if i < limit:
            result.append(i)
    return print(result)

filter_values_above_4(lista, 4)