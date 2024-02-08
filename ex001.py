# Fazer um Algoritmo estruturado para:
# Soma de dois numeros X
# Append de 2 letras X
# Usar input do usuário X
# Utilizar estruturas de repetição
#   - While, Do While, For X
# Utilizar estruturas condicionais
#   - IF X, Else, Elif
# Fatorial
#


print("Soma de dois numeros")
num1 = int(input("digite o primeiro numero para somar"))
num2 = int(input("digite o segundo numero para somar"))
print(num1+num2)

print("Append de 2 letras")
lista = []
letra_add=input("Digite uma letra para adicionar na lista")
letra_add2=input("Digite uma letra para adicionar na lista")

lista.append(letra_add)
lista.append(letra_add2)
print(lista)

print("Utilizar estruturas de repetição e condicional")
user1 = int(input("Digite um número:"))
user2 = input("Digite uma letra:")

if user1 < 0:
    print("erro")
else:
    for user1 in user2:
        print(user1)

# while