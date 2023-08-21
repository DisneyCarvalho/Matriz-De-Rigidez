import numpy as np

class Treliças ():

    def __init__(self, area,moduloElasticidade):
        #Na matriz "no" estão os nós da barra com a posição x e y

        self.area = 1
        self.moduloElasticidade = 1
        self.mGlobal = None
        self.mmLocal = []


    def lambidas (self):
        lambx = []
        lamby = []
        l = []
        n = self.numBarras
        for i in range (n):
            for j in range(0,len(self.nos[i]),2):
                nx = self.nos[i][j][0]
                ny = self.nos[i][j][1]
            for o  in range(1,len(self.nos[i]),2):
                fx = self.nos[i][o][0]
                fy = self.nos[i][o][1]

            l.append((((fx-nx)**2) + ((fy-ny)**2))**(1/2))

            lambx.append((fx - nx)/l[i])

            lamby.append((fy - ny)/l[i])

            print(l[i], lambx[i], lamby[i])
        return lambx, lamby, l


    def lambdaADJC(self,nos, ligacoes):
        self.large = []
        self.lambx = []
        self.lamby = []
        for i in range(0,len(ligacoes)):
            for j in range(i+1,len(ligacoes[i])):
                if ligacoes[i][j] == 1:
                    self.large.append((((nos[j][0]-nos[i][0])**2) + ((nos[j][1]-nos[i][1])**2))**(1/2))

                    self.lambx.append(((nos[j][0] - nos[i][0]) / self.large[len(self.large)-1]))

                    self.lamby.append(((nos[j][1] - nos[i][1]) / self.large[len(self.large)-1]))
                    posil = (i*2+1,i*2+2)
                    posicol = (j*2+1,j*2+2)


        self.numBarras = len(self.large)




    def matrizLocal(self): #Falta generalizar essa função para n nós
        n = self.numBarras
        lambidas = self.lambidas()
        for i in range (n):
            lambx = lambidas[0][i]
            lamby = lambidas[1][i]
            l = lambidas[2][i]
            print("Valores de: ",lambx,lamby,l)
            mLocal = np.array([
                [lambx**2, lamby*lamby, -lambx**2, -lambx*lamby],
                [lambx*lamby, lamby**2, -lambx*lamby, -lamby**2],
                [-lambx**2, -lamby*lamby, lambx**2, lambx*lamby],
                [-lambx*lamby, -lamby**2, lambx*lamby, lamby**2],
            ])
            #Pesquisar sobre o numpy
            mLocal = (self.area*self.moduloElasticidade/l)*mLocal
            self.mmLocal.append(mLocal)
            print(mLocal)

        return mLocal




    def matrizLocalADJC(self): #Falta generalizar essa função para n nós
        n = self.numBarras
        mmLocal = []
        for i in range (n):
            lambx = self.lambx[i]
            lamby = self.lamby[i]
            l = self.large[i]
            #print("Valores de: ",lambx,lamby,l)
            mLocal = np.array([
                [lambx**2, lamby*lamby, -lambx**2, -lambx*lamby],
                [lambx*lamby, lamby**2, -lambx*lamby, -lamby**2],
                [-lambx**2, -lamby*lamby, lambx**2, lambx*lamby],
                [-lambx*lamby, -lamby**2, lambx*lamby, lamby**2],
            ])
            #Pesquisar sobre o numpy
            mLocal = (self.area*self.moduloElasticidade/l)*mLocal
            mmLocal.append(mLocal)
            print(mLocal)
        #print(mmLocal)
        return mmLocal

    def matrizGlobal (self,nos,posilinha,posicoluna,mlocal):

        if self.mGlobal == None:
            self.mGlobal = np.zeros([len(nos)*3,len(nos)*3])



        for i in range(len(mlocal)):
            for j in range(len(mlocal)):
                self.mGlobal[posilinha[i]][posicoluna[j]] += mlocal[i][j]















