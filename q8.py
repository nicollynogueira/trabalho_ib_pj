número1 = int(input("Digite um número: "))
número2 = int(input("Digite outro número: "))
soma = número1 + número2
subtração = número1 - número2
multiplicaçao = número1 * número2
divisão = número1 / número2 if número2 !=0 else "Indefinido (div. por 0)"
print(f"soma:{número1} + {número2} = {soma} ")
print(f"subtração:{número1} - {número2} = {subtração}")
print(f"multiplicaçao:{número1} * {número2} = {multiplicaçao}")
print(f"divisão: {número1} / {número2} = {divisão}")