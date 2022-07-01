
from cmath import log
import cmath

def vetorinf(matriz_teste, KEY):
    """4. vetor que será utilizado, KEY é a linha que será analisada"""
    aux = {}
    Y = ""
    for i in matriz_teste.keys():
        for j in range(len(matriz_teste[i])):
            if(j == KEY):
                aux[i]= matriz_teste[i][j]
                if matriz_teste[i][j]=="": Y = i

    return aux, Y

def ctclasse(matriz_treinamento, Y, classe):
    cont_classe={}
    for i in matriz_treinamento[Y]:
        if i == classe:
            if Y in cont_classe:
                cont_classe[Y] += 1
            else:
                cont_classe[Y] = 1
    return cont_classe

def probs(matriz_treinamento , aux, Y, classe, ctclasse):
    """5. construção das probabilidades /precisa de uma limpeza de cósigo"""
    cont_ocorrencias = {}
    cont_colunas={}

    
    #dos valores
    auxkeys = [*aux]
    for j in range(len(aux)):
        for i in matriz_treinamento[auxkeys[j]]:
            if auxkeys[j] != Y:
                cont_ocorrencias[aux[auxkeys[j]]] = 1
    for j in range(len(cont_ocorrencias)):
        cont=0
        for i in matriz_treinamento[auxkeys[j]]:
            if aux[auxkeys[j]] == i and matriz_treinamento[Y][cont]==classe:
                cont_ocorrencias[aux[auxkeys[j]]] +=1
            cont+=1
    
    cont_classe=ctclasse(matriz_treinamento, Y, classe)

    V= len(cont_ocorrencias)

    #naive:
    total = 0.0
    for i in cont_ocorrencias.keys():
        
        x= cont_ocorrencias[i]/(V+cont_classe[Y])
        cont_colunas[i]=log(x,10)
        total+= cont_colunas[i]
    return total.real   
    



def naive(matriz_treinamento, Y, aux, ctclasse):
    #contagem de classes:
    classe={}
    for i in matriz_treinamento[Y]:
        classe[i]=0
    classe1 = classe.copy()
    #print(len(classe))
    for i in classe1:
        cont_classe = ctclasse(matriz_treinamento, Y, i)
        x = cont_classe[Y]/len(matriz_treinamento[Y])
        classe1[i]=log(x,10).real 

    for i in classe.keys():
        classe[i] = round(classe1[max(classe1)] + probs(matriz_treinamento , aux, Y, i, ctclasse),4)      
        #print(log(x,10).real)    
    #print(classe['seguro']>classe['perigoso'])   

    max_value = None
    for num in classe.keys():
        if (max_value is None or classe[num] > max_value):
            max_value = classe[num]
            maxkey = num
    print(maxkey)

    #print(cont_ocorrencias)
    #print(V)
    """       
    prob_aprioriX = cont_ocorrencias.copy()
    
    for i in cont_ocorrencias.keys():
        prob_aprioriX[i]=prob_aprioriX[i]/(len(matriz_treinamento[Y])+1)
    
    #dos y
    for i in matriz_treinamento[Y]:
        if i in cont_ocY:
            cont_ocY[i] += 1
        else:
            cont_ocY[i] = 1
    prob_aprioriY = cont_ocY.copy()
    for i in prob_aprioriY.keys():
        prob_aprioriY[i]=prob_aprioriY[i]/len(matriz_treinamento[Y])
    
    #prob da interseção
    auxY = []
    auxa = []
    for i in aux.keys():
        if(i != Y):
            for j in range(len(matriz_treinamento[Y])):  
                #print(matriz_treinamento[i][j] == aux[i],"\n")
                #print(matriz_treinamento[i][j],"\n")
                #print(aux[i],"\n\n")              
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
    return cont_ocY, prob_aposteriori, auxY, prob_aprioriY"""

"""def naivebayes(cont_ocY, prob_aposteriori, auxY, prob_aprioriY):
    #6. o naive bayes de fato
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
    
    maxkey=max(prob_naiveY, key=prob_naiveY.get)
    return maxkey"""