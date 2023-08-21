from treliças import Treliças
import verificações
import m_Adjacência2 as ma



if __name__ == '__main__':
    a = Treliças(0,0)

    b = ma.matriz_adjacencias()
    nos = ma.nos()
    a.lambdaADJC(nos,b)

    print(len(a.matrizLocalADJC()))

    a.matrizGlobal(nos)



