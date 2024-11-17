
lista = [1, 2, 4, 5]

def find_missing_values(lista: list[int]) -> list[int]:
    n = 0
    for i in lista:
        if lista[n] + lista[n+1] != lista[n+2]:
            lista.append(lista[n] + lista[n+1])
            lista = sorted(lista)
    n = n + 1
    return print(lista)

find_missing_values(lista)