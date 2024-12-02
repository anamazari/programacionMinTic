numeros = []

for n in range(10):   
    numeros.append(n+1) 

i = 1
while n < 10:
    if numeros[i] % 2 == 0:
       numeros.remove(numeros[i]) 
    print(numeros[i])
    i += 1







