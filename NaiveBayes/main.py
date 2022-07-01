import data_processing as dp
import naive_bayes as nb
from datas import matrices as mt
#montagem do código
#fornecendo o nome do arquivo:
nome_arquivo = "NaiveBayes/datas/datase01.csv"
matriz_treinamento, matriz_teste = dp.construcao(nome_arquivo)
classe="seguro"

for i in range(len(matriz_teste[next(iter(matriz_teste))])):

    aux, Y = nb.vetorinf(matriz_teste, i)

    maxkey= nb.naive(matriz_treinamento, Y, aux, nb.ctclasse)
    print(classe)

    print("\n\n",("#"*40),"\n\nDadas as informações:\n",)
    for i in aux.keys():
        if(i != Y):
            print(i,": ",aux[i])
    print("\nA predição para o resultado de ",Y," é: ",maxkey,"\n")