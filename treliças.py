import numpy as np
import math

class Treliças ():

    def __init__(self, area,moduloElasticidade):
        #Na matriz "no" estão os nós da barra com a posição x e y

        self.area = 1
        self.moduloElasticidade = 1
        self.mGlobal = np.array([])
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
        ia = 0
        for i in range(0,len(ligacoes)):
            for j in range(i+1,len(ligacoes[i])):
                if ligacoes[i][j] == 1:
                    large = (((nos[j][0]-nos[i][0])**2) + ((nos[j][1]-nos[i][1])**2))**(1/2)
                    self.large.append(large)

                    lambx = ((nos[j][0] - nos[i][0]) / self.large[len(self.large)-1])
                    self.lambx.append(lambx)

                    lamby = ((nos[j][1] - nos[i][1]) / self.large[len(self.large)-1])
                    self.lamby.append(lamby)

                    posil = (i*2,i*2+1)
                    posicol = (j*2,j*2+1)

                    mlocal = self.matrizLocalADJC(lambx,lamby,large,posil,posicol)
                 #   if ia < 4:
                  #      print("Matriz local adadadada\n", mlocal)
                    self.matrizGlobal(nos,posil,posicol,mlocal)

                    ia += 1






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




    def matrizLocalADJC(self,lambx,lamby,large,posil,posicol):

        lambx = lambx
        lamby = lamby
        l = large

        mLocal = np.array([
            [lambx**2, lamby*lamby, -lambx**2, -lambx*lamby],
            [lambx*lamby, lamby**2, -lambx*lamby, -lamby**2],
            [-lambx**2, -lamby*lamby, lambx**2, lambx*lamby],
            [-lambx*lamby, -lamby**2, lambx*lamby, lamby**2],
        ])

        mLocal = (self.area*self.moduloElasticidade/l)*mLocal
        self.mmLocal.append(mLocal)

        return mLocal





    def setCor(self,i,j,cores):

        if math.floor(i/2) % 2 == 0: #Linha par 11
            return cores[math.floor((j / 2) +3) % 8]


        if math.floor(i/2) % 2 == 1:  ##linha Impar
            return cores[math.floor(j / 2) % 8]




    def pritglob(self):
        cores = ['\033[0;0m \033[37m', '\033[0;0m \033[36m', '\033[1m \033[30m', '\033[0;0m \033[33m', '\033[0;0m \033[35m', '\033[0;0m \033[34m', '\033[0;0m \033[32m', '\033[0;0m \033[31m']

        for i in range(len(self.mGlobal)):
            for j in range(len(self.mGlobal)):
                cor = self.setCor(i,j,cores)
                print(f"{cor}[{round(self.mGlobal[i][j],1):^6}]",end="")
            print()

    def matrizGlobal (self,nos,posilinha,posicoluna,mlocal):

        if len(self.mGlobal) == 0:
            self.mGlobal = np.zeros([len(nos)*2,len(nos)*2])



        for i in range(len(posilinha)):
            for j in range(len(posilinha)):
                self.mGlobal[posilinha[i]][posilinha[j]] += mlocal[i][j]


        for i in range(len(posicoluna),len(mlocal)):
            for j in range(len(posicoluna),len(mlocal)):
                self.mGlobal[posicoluna[i-len(posicoluna)]][posicoluna[j-len(posicoluna)]] += mlocal[i][j]


        for i in range(len(posilinha)):
            for j in range(len(posicoluna),len(mlocal)):
                self.mGlobal[posilinha[i]][posicoluna[j-len(posicoluna)]] += mlocal[i][j]



        for i in range(len(posicoluna),len(mlocal)):
            for j  in range(len(posicoluna)):
                self.mGlobal[posicoluna[i-len(posicoluna)]][j] += mlocal[i][j]



















