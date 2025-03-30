turmas = int(input("Informe a quantidade de turmas: "))
alunos = int(input("Informe a quantidade total de alunos: "))
med = alunos // turmas
if med > 40:
    print(f"Atencao, a media é superior a 40 alunos, com um total de {media}.")
else:
 print(f"A media de alunos por turma é {media}.")
