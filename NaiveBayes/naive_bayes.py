
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
    for i in classe1:
        cont_classe = ctclasse(matriz_treinamento, Y, i)
        x = cont_classe[Y]/len(matriz_treinamento[Y])
        classe1[i]=log(x,10).real 

    for i in classe.keys():
        classe[i] = round(classe1[max(classe1)] + probs(matriz_treinamento , aux, Y, i, ctclasse),4)      

    max_value = None
    for num in classe.keys():
        if (max_value is None or classe[num] > max_value):
            max_value = classe[num]
            maxkey = num
    return maxkey
