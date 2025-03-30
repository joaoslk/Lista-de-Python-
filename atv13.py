salario_inicial = int(input("Informe seu salario inicial: "))
tempo = int(input("Informe a quantos anos voce trabalha: "))
salario_final = salario_inicial * (2 ** tempo)
print(f"Seu salario apos um tempo de {tempo} anos de servico sera: {salario_final}.")
