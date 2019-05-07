
#%%
def somaPartes(entrada):
    valor = 0    
    if entrada != "":
        partes = entrada.split("+")
        for i in partes:
            valor = valor + float(i)
    return valor    


print(f'{entrada} = {somaPartes(entrada)}')
#%%
entrada = "4+5.5+9+3.5"
partes = entrada.split("+")
for i in range(len(partes)):
    print(float(partes[i]))