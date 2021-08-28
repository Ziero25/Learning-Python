n = int(input("Digite um número:"))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O Dobro de {} vale {}.".format(n, d))
print("O Triplo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}".format(n, t, n, r))

print("O Dobro de {} vale {}.".format(n, (n * 2)))
print("O Triplo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}".format(n, (n * 3), n, (n ** (1/2))))
