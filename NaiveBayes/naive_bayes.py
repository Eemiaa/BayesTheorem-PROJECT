
from cmath import log
from genericpath import exists


def vetorinf(matriz_teste, KEY):
    aux = {}
    Y = ""
    for i in matriz_teste.keys():
        for j in range(len(matriz_teste[i])):
            if(j == KEY):
                aux[i]= matriz_teste[i][j]
                if matriz_teste[i][j]=="": Y = i

    return aux, Y

def probs(matriz_treinamento , aux, Y):
    cont_ocorrencias = {}
    cont_ocY = {}
    cont_intersecao={}

    #dos valores
    auxkeys = [*aux.keys()]
    for j in range(len(aux)):
        for i in matriz_treinamento[auxkeys[j]]:
            if aux[auxkeys[j]] == i:
                if aux[auxkeys[j]] in cont_ocorrencias: 
                    cont_ocorrencias[aux[auxkeys[j]]] +=1
                else:
                    cont_ocorrencias[aux[auxkeys[j]]] = 1
    prob_aprioriX = cont_ocorrencias.copy()
    for i in cont_ocorrencias.keys():
        prob_aprioriX[i]=prob_aprioriX[i]/len(matriz_treinamento[Y])
    #dos y
    for i in matriz_treinamento[Y]:
        if i in cont_ocY:
            cont_ocY[i] += 1.0
        else:
            cont_ocY[i] = 1.0
    prob_aprioriY = cont_ocY.copy()
    for i in prob_aprioriY.keys():
        prob_aprioriY[i]=prob_aprioriY[i]/len(matriz_treinamento[Y])
    
    #prob da interseção
    auxY = []
    auxa = []
    for i in aux.keys():
        if(i != Y):
            for j in range(len(matriz_treinamento[Y])):  
                """print(matriz_treinamento[i][j] == aux[i],"\n")
                print(matriz_treinamento[i][j],"\n")
                print(aux[i],"\n\n") """               
                if (matriz_treinamento[i][j] == aux[i]):
                    auxx = matriz_treinamento[i][j]+"|"+matriz_treinamento[Y][j]
                    if auxx in cont_intersecao.keys():
                        cont_intersecao[auxx]+=1
                    else: 
                        auxY.append(matriz_treinamento[Y][j])
                        auxa.append(matriz_treinamento[i][j])
                        cont_intersecao[auxx]=1
                    
    prob_aposteriori = cont_intersecao.copy()
    auxXY = list(prob_aposteriori.keys())

    for i in range(len(prob_aposteriori)):
        #print(cont_ocY[auxY[i]])
        prob_aposteriori[auxXY[i]]=prob_aprioriX[auxa[i]]*(prob_aposteriori[auxXY[i]]/cont_ocY[auxY[i]])
    
    return cont_ocY, prob_aposteriori, auxY, prob_aprioriY

def naivebayes(cont_ocY, prob_aposteriori, auxY, prob_aprioriY):
    #print(cont_ocY)
    import cmath 
    aux = {}
    keysap = list(prob_aposteriori.keys())
    prob_naiveY={}
    for i in cont_ocY.keys():
        #somatorio:
        for j in range(len(prob_aposteriori.keys())):
            if auxY[j] in aux.keys():
                aux[auxY[j]]= aux[auxY[j]] + log(prob_aposteriori[keysap[j]],10)
            else:
                aux[auxY[j]]= log(prob_aposteriori[keysap[j]],10)
        prob_naiveY[i]= log(prob_aprioriY[i],10) + aux[i]
        prob_naiveY[i] = prob_naiveY[i].real
    
    print(max(prob_naiveY, key=prob_naiveY.get))

