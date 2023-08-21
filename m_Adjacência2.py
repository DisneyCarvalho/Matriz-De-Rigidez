import numpy as np

comprimento = 4
dist_barras_verticais = 1
altura_treliça = 0.5
inclinação = 5

def nos():
    if comprimento%2 ==0:
        #Código responsável pela criação dos nós
        n =2 + 2*int(comprimento/dist_barras_verticais)
        no = np.zeros([n,2])
        j = 2 #A variável j é responsável por decrementar a altura apos passar pelo monto do meio da treliça

        for i in range(0,n,2):
            if i<=n/2:#Para preencher o lado esquerdo
                #Criação dos nós inferiores
                no[i][0] = dist_barras_verticais*(i/2)
                no[i][1] = (i/2)*inclinação/100
                #Criação dos nós superiores
                no[i+1][0] = dist_barras_verticais * (i/2)
                no[i+1][1] = ((i/2) * inclinação / 100) + altura_treliça
            else:#para preencher o lado direito
                #A ideia é fazer um decremento da altura maxima causada pela inclinação
                imax = ((comprimento/2) * inclinação / 100) #ponto mais alto do banzo inferior
                # Criação dos nós inferiores
                no[i][0] = dist_barras_verticais * (i / 2)
                no[i][1] =imax - ((int(j / 2)) * inclinação / 100)
                # Criação dos nós superiores
                no[i + 1][0] = dist_barras_verticais * (i / 2)
                no[i + 1][1] = imax - (int(j / 2) * inclinação / 100) + altura_treliça
                j= j+2
        return no
    else:
        return print("Não é possível montar a matriz devido da dispisição das barras")

def matriz_adjacencias():
    n = comprimento*2 +2
    m_adjacencia = np.zeros([n,n])
#Condição para os dois primeiros nós
    #para o primeiro nó
    m_adjacencia[0][1] = 1
    m_adjacencia[0][2] = 1
    #para o segundo nó
    m_adjacencia[1][0] = 1
    m_adjacencia[1][2] = 1
    m_adjacencia[1][3] = 1
#Demais nós da esquerda
    if comprimento >2:
        for i in range(comprimento-2):
            m_adjacencia[i+2][i] = 1
            m_adjacencia[i+2][i+1] = 1
            m_adjacencia[i+2][i+3] = 1
            m_adjacencia[i+2][i+4] = 1
#Para os nós do meio
    #Para o nó inferior
    m_adjacencia[comprimento][comprimento-2] = 1
    m_adjacencia[comprimento][comprimento-1] = 1
    m_adjacencia[comprimento][comprimento+1] = 1
    m_adjacencia[comprimento][comprimento+2] = 1
    m_adjacencia[comprimento][comprimento+3] = 1
    #Para moldar o nó superior
    m_adjacencia[comprimento+1][comprimento-1] = 1
    m_adjacencia[comprimento+1][comprimento-0] = 1
    m_adjacencia[comprimento+1][comprimento+3] = 1
#Para os dois ultimos nós
    #Para o nó inferior
    m_adjacencia[n-2][n-4] = 1
    m_adjacencia[n-2][n-1] = 1
    #Para o nó superior
    m_adjacencia[n-1][n-2] = 1
    m_adjacencia[n-1][n-3] = 1
    m_adjacencia[n-1][n-4] = 1
#Para os demais nós da direita
    if comprimento >2:
        for i in range(0,comprimento-2,2):
            #Para o nó inferior
            s = i*2 + 2
            m_adjacencia[comprimento+s][comprimento+(i*2)] = 1
            m_adjacencia[comprimento+s][comprimento+(i*2) +3] = 1
            m_adjacencia[comprimento+s][comprimento+(i*2) +4] = 1
            m_adjacencia[comprimento+s][comprimento+(i*2) +5] = 1
            #Para o nó superior
            m_adjacencia[comprimento+s+1][comprimento+(i*2)] = 1
            m_adjacencia[comprimento+s+1][comprimento+(i*2)+1] = 1
            m_adjacencia[comprimento+s+1][comprimento+(i*2)+2] = 1
            m_adjacencia[comprimento+s+1][comprimento+(i*2)+5] = 1


    return m_adjacencia

if __name__ == "__main__":
    a = nos()
    b = matriz_adjacencias()
    print(a)
    print(b)