import data_processing as dp
import naive_bayes as nb
from datas import matrices as mt
#montagem do código
#fornecendo o nome do arquivo:
nome_arquivo = "NaiveBayes/datas/datase01.csv"
matriz_treinamento, matriz_teste = dp.construcao(nome_arquivo)
classe="seguro"
#print(len(matriz_teste[next(iter(matriz_teste))]))

for i in range(len(matriz_teste[next(iter(matriz_teste))])):
    aux, Y = nb.vetorinf(matriz_teste, i)

    #cont_ocY, prob_aposteriori, auxY, prob_aprioriY = 
    #cont_colunas, total=nb.probs(matriz_treinamento , aux, Y,classe)
    #maxkey = nb.naivebayes(cont_ocY, prob_aposteriori, auxY, prob_aprioriY)
    #dp.insercao(maxkey, aux, Y)

    nb.naive(matriz_treinamento, Y, aux, nb.ctclasse)



    """print(("#"*40),"\n\nDadas as informações:\n",)
    for i in aux.keys():
        if(i != Y):
            print(i,": ",aux[i])
    print("\nCom as probabilidades aposteriories:\n")
    for i in prob_aposteriori.keys():
        print(i,": ",prob_aposteriori[i])

    print("\nA predição para o resultado de ",Y," é: ",maxkey,"\n")
    """