rod = '~'*50
cab = '_'*50
#SubProgramas

#Preenche os dados a serem buscados
def preencher(valores):
    print(f'Recebendo {len(valores)} valores ...')
    for i in range(len(valores)):
        print(cab)
        valores[i] = input("Digite um valor inteiro: \n")
        print(f'O valor {valores[i]} foi adicionado \n Restam {len(valores)-1 - i} valores a serem adicionados')
    print(f'A lista foi preenchida da seguinte forma: \n {valores} \n {rod}')
    return None

#Busca na lista com os dados um elemento da lista definido pelo usuário
def buscaElemento(valores,procurado):
    i = 0
    while valores[i] != procurado:
        i+=1
        if i==len(valores)-1:
            local = -1
        else:
            local = i
    return local

def escreveResposta(dado,pos):
    if pos != -1:
        print(f'{cab} \n Resultado para a busca: \n Elemento {dado} encontrado na posição {pos} \n {rod}')
    else:
        print(f'Elemento {dado} não localizado')
# Escreve o resultado da busca.
#PRINCIPAL

print(cab)
print('programa de busca simples')
print(rod)
numeros=[0]*10
preencher(numeros)
dado = input("Digite o elemento a ser procurado \n")
numeros.append(dado)
onde = buscaElemento(numeros,dado)
escreveResposta(dado, onde)
