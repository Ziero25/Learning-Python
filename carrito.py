km = float(input("Digite quantos km o carro percorreu: "))
dias = int(input("Digite por quantos dias ele ficou alugado: "))

kmresultado = km * 0.15
diasresultado= dias * 60

print(f"Você pagará R${kmresultado + diasresultado} pela utilização do carro alugado.")
