def somaNotas(qtdNotas):
    listaNotas = []
    for x in range(1, qtdNotas+1): ##notas para cada quantidade colocada##
        nota = float(input("Entrada de notas "+str(x)+": ")) ##define o valor de cada nota para a quantidade de notas##
        listaNotas.append(nota) ##Armazenar notas no vetor##
    return listaNotas##Retornar o vetor de notas informadas##
qtdeNotas = int(input("Digite as quantidades de notas que deseja colocar no sistema: \n")) ##Define a quentidade de notas que serão informadas##
soma = 0
for nota in somaNotas(qtdeNotas):
    soma += nota ##Somar as notas determinadas presentes no metodo somaNotas##
print("Média: "+str(soma/qtdeNotas))##Média das notas##
if ((soma/qtdeNotas) < 7):
    print("Você está com média insuficiente para passar")
else:
    print("Parabéns pela sua média!")