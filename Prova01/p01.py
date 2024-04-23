numeros = []
x = 0

for i in range(3):
    x=int(input(f"Digite numero"))
    numeros.append(x)

numeros.sort(reverse = True)
print(numeros)

