#importando as funções específicas de um módulo.


from math import ceil, floor, factorial




numero = float(input("Digite um número quebrado: "))
print(f"Para cima: {ceil(numero)}")
print(f"Para baixo:{floor(numero)}")
print(f"Fatorial: ! {factorial(int(numero))}")


#import math
"""
numero = float(input("Digite um número quebrado: "))
print(f"Para cima: {math.ceil(numero)}")
print(f"Para baixo:{math.floor(numero)}")
print(f"Fatorial: ! {math.factorial(int(numero))}")
"""