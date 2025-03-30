number = int(input("Diga um numero impar:"))
anterior = number - 2
num_anterior = anterior * anterior
posterior = number + 2
num_posterior = posterior * posterior
dif_anterior = num_anterior - number
dif_posterior = num_posterior - number 
print(f"Diferenca do quadrado do anterior: {dif_anterior}.")
print(f"Diferenca do quadrado do posterior: {dif_posterior}.")
