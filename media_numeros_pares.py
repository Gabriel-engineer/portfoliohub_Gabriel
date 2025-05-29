numeros_pares = []

print("Digite 0 para sair")
while True:
    valor = int(input("valor: "))
    if valor == 0:
        break
    if valor % 2 == 0:
        numeros_pares.append(valor)

if numeros_pares:
    soma_par = sum(numeros_pares)
    qtd_par = len(numeros_pares)
    media_par = soma_par / qtd_par
    print("Média dos pares:", media_par)
print("media pares:", sum(numeros_pares)/len(numeros_pares))
print(f"valores pares digitados:\n{numeros_pares}")
print("valores na vertical")
for pares in numeros_pares:
    print(pares)
if len(numeros_pares) > 0:
    print("media dos pares:", sum(numeros_pares)/len(numeros_pares))
else:
    print("não foi digitado numero par.")



