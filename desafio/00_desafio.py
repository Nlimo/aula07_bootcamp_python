from etl import ler_csv, filtrar_produtos_entregues, somar_valores

pah = 'desafio/vendas.csv'

arquivo = ler_csv(pah)
arquivo2 = filtrar_produtos_entregues(arquivo)
result = somar_valores(arquivo2)

print(result)