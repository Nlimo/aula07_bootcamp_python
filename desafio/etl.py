# Função para ler o arquivo CSV
import csv

pah = 'desafio/vendas.csv'

def ler_csv(nome_arquivo):
    lista = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha) 
        return lista


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Listar produtos que não foram entregues
    """
    lista_item_filtro = []
    for item in lista:
        if item.get('entregue') == "False":
            lista_item_filtro.append(item)
    return lista_item_filtro


def somar_valores(lista_item_filtro: list[dict]) -> float:
    """
    Soma de valores
    """
    result_def_somar_valores: float 
    valor_total: float = 0
    for valor in lista_item_filtro:
        valor_total += float(valor.get("preco"))
    return valor_total

arquivo = ler_csv(pah)
arquivo2 = filtrar_produtos_entregues(arquivo)
result = somar_valores(arquivo2)

print(result)