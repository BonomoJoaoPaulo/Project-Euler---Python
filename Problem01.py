
soma = 0

for n in range(1000):
    if (n%3 == 0) or (n%5 == 0):
        soma += n

print(soma)