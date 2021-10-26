
lista_primos = []

def teste_primo(n):
    divisores = 0
    primo = False
    for v in range(1, n+1):
        if (n % v == 0):
            divisores += 1
    if divisores > 2:
        primo = False
    elif n == 1:
        primo = False
    else:
        primo = True
    return primo

for n in range(1,10000000000000):
    teste = teste_primo(n)
    if teste:
        lista_primos.append(n)
    if len(lista_primos) == 10001:
        print(lista_primos[10000])
        break


