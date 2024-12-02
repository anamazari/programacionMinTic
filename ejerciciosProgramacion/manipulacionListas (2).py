#numeros = []

#for n in range(10):   
    #numeros.append(n) 

#i = 1
#while i < 10:
    #if numeros[i] % 2 == 0:
       #numeros.remove(numeros[i]) 
    #print(numeros[i])
    #i += 1


numeros = []
for n in range(1,11):   
    numeros.append(n) 

i = 0
while i < 10:
    print(numeros[i])
    i += 1

for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)

print(numeros)










