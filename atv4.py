distancia = int(input("Diga a distancia percorrida:"))
tempo = int(input("Diga o tempo que o carro foi alugado:"))
if distancia > 100:
 taxa = (distancia - 100) * 12
 valor = tempo * 90 + taxa
 print(f"Valor com taxa por quilometros excedidos: {valor}")
else:
 valor = tempo * 90
 print(f"Valor total: {valor}")
