
for num in range(1000000):
    inverso = (str(num)[::-1])
    inverso = int(inverso)
    if num == inverso:
        for n1 in range(100,1000):
            for n2 in range(100,1000):
                if num == n1*n2:
                    print(num)