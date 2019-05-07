

#%%
def criaLista():
    lista=[]
    produto=input("Produto: ")
    while produto != "fim":
        qtd=int(input("Quantidade: "))
        valUni=float(input("Valor Unitário: "))
        lista.append((produto,qtd,valUni))
        produto=input("Produto: ")
    return lista
#%%
def processa(compra):
    total=0.0
    for(produto,qtd,valUni) in compra:
        total = qtd * valUni
        print(f'Produto: {produto} | Quantidade: {qtd} | Preço Unitário: {valUni}')
    print(f'Total = {total}')
    return None
#%%
compras = criaLista()
print(compras)
processa(compras)