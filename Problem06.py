s1 = 0
s2 = 0

for n in range (1, 101):
    s1 += (n**2)

for m in range(1,101):
    s2 += m

resp = (s2**2)-s1

print(resp)
