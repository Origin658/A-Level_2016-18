#V.1


number = 20
factors = []
for i in range(1, number+1):
    if number%i == 0:
        factors.append(i)
print(factors)