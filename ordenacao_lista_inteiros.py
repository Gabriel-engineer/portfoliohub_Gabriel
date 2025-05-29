lista = []
print('Digite 0 para sair')
while True:
    valor = int(input("Valor inteiro: "))
    if valor == 0:
        break
    lista.append(valor)

print(lista)
lista.sort()

print("\nNumeros digitados em ordem crescente:")
print(lista)
print("menor",lista[0])
print("maior",lista[-1])
print("valores na lista na horizontal\n", lista)
print("valores na vertical")
for elemento in lista:
    print(elemento)
print("indice-valores na vertical")
ct = 0
for elemento in lista:
    print(ct, "-",elemento)
    ct +=1
print("indice-valores na vertical")
for elemento in lista:
    print(lista.index(elemento),"-",elemento)

