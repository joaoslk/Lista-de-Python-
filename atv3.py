preco = int(input("Diga o valor das compras:"))
if preco > 500:
    taxa = (preco - 500) * 1.5
    valor_taxado = taxa + 500
    print(f"Valor com taxa de 50%: {valor_taxado}")
else:
    print("Livre de taxa")
