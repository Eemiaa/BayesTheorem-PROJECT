import csv

"""leitura do arquivo csv"""
def leitura(treinamento): 
    #abrir arquivo
    with open(treinamento, encoding='utf-8') as aqr_treinamento:
        #ler tabela
        aux_mat = []    
        tab_treinamento = csv.reader(aqr_treinamento, delimiter=',')
        #dividir o arquivo em dois
        aux_mat = list(tab_treinamento)
        aux_teste, aux_treino = [],[]
        aux_teste.append(aux_mat[0])
        aux_treino.append(aux_mat[0])
        for i in range(len(aux_mat)):
            if(i>0):
                if "" in aux_mat[i]:
                    aux_teste.append(aux_mat[i])
                else:
                    aux_treino.append(aux_mat[i])
        return aux_teste, aux_treino

def tratamento(aux_mt):
    matriz={}
    for coluna in range(len(aux_mt[0])):
            matriz[aux_mt[0][coluna]]=[]
            aux=[]
            for linha in range(len(aux_mt)):
                if(linha>0): 
                    aux.append(aux_mt[linha][coluna].replace(" ", "")) 
            matriz[aux_mt[0][coluna]]=aux        
    return matriz    

def construcao(treinamento):
    from datas import matrices as mt
    aux_teste, aux_treino = leitura(treinamento)
    mt.matriz_treinamento = tratamento(aux_treino)
    mt.matriz_teste = tratamento(aux_teste)
    return mt.matriz_treinamento, mt.matriz_teste
