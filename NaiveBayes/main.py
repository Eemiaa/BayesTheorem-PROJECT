import data_processing as dp
import naive_bayes as nb

treinamento = "NaiveBayes/datas/datase01.csv"

matriz_treinamento, matriz_teste = dp.construcao(treinamento)

aux, Y = nb.vetorinf(matriz_teste, 0)
cont_ocY, prob_aposteriori, auxY, prob_aprioriY = nb.probs(matriz_treinamento , aux, Y)
nb.naivebayes(cont_ocY, prob_aposteriori, auxY, prob_aprioriY)
#print(matriz_treinamento)
