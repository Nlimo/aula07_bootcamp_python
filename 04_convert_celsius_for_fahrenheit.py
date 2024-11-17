lista = [30, 18, 24]

def convert_celsius_for_fahrenheit(lista: list) -> list[float]:
    lista_fahrenheit = []
    for i in lista:
        lista_fahrenheit.append(i * 9/5 + 32)
    return print(lista_fahrenheit)

convert_celsius_for_fahrenheit(lista)