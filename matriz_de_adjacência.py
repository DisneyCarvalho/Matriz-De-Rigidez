nos = [
    [0,0.00],
    [0,0.50],
    [1,0.05],
    [1,0.55],
    [2,0.00],
    [2,0.50]
]
print(len(nos))

def no_mais_alto(nos): #Função para determinar o nó mais alto que será o pai
    no_topo = [0,0]
    for i in range(0,len(nos)):
        if no_topo[1] <= nos[i][1]:
            no_topo = nos[i]
    return no_topo
def comprimento_da_treliça():
    pass
def altura_da_treliça():
    pass
def distancia_entre_as_barras_verticais():
    pass
if __name__ == "__main__":
    a = no_mais_alto(nos)
    print(a)