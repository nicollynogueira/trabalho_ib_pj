nome = input("Digite o seu nome: ") 
disciplina = input("Digite sua disciplina: ") 
n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: ")) 
m = (n1 + n2)/2
if (m)>5:
    print(f"Você {nome} está aprovado em {disciplina} com média {m}")
else:
    print(f"Você {nome} está reprovado em {disciplina} com média {m}")
