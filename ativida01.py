# Crar um objeto chamado Geladeira que cabe 10 litros de leite. 
# Depois, criem uma Thread chamado BebeLeite que dorme (por um tempo aleatório) e quando acorda bebe 1 litro de leite... 
# e 3 Threads (Pai, Mae e Tio) que monitoram a geladeira... eles vêem quanto tá faltando e compra mais Leite.... Dessa forma, vai haver um momento em que eles vão comprar mais leite do que cabe na geladeira... quero que vocês lançem um alerta quando isso ocorrer.. a idéia é demonstrar que a "região crítica" não foi bem tratada, e que temos um problema neste ponto. 


from random import randint
from threading import *		
import time		

paiContador = 0
maeContador = 0
tioContador = 0 

class Geladeira:
    def __init__(self):
        self.qntdLeite = 10
        self.emFalta = False
    
    def beberLeite(self):
        self.qntdLeite -= 1
        # dormirPor = randint(1,3)
        # while self.qntdLeite > 0:
        #     time.sleep(dormirPor)
        #     self.qntdLeite -= 1
        #     self.emFalta = True
        #     print(self.qntdLeite)
        
    def adicionaLeite(self):
        if self.qntdLeite < 10 and self.emFalta == True:
            self.qntdLeite += 1
        else:
            print('ENCHEU ENCHEU ENCHEU, TA BOM TA BOM, PARA PARA')

class Pessoa:
    def __init__(self):
        self.comprou = 0
    
    def comprar(qntd):
        self.comprou += qntd 


gelada = Geladeira()
geladaObj = Semaphore()
print(gelada)

def mainBeberLeite():
    dormirPor = randint(1,10)
    gelada.beberLeite()
    for i in range (10):
        time.sleep(dormirPor)
        gelada.beberLeite()
        print('bebendo 1 litrinho...')
        gelada.emFalta = True
        print(gelada.qntdLeite)

def monitora(familiar):
    geladaObj.acquire()
    print(gelada.emFalta)
    print(gelada.qntdLeite)
    print('aqui')
    for i in range (10):
        print(f'em {i}, a geladeira tem: {gelada.qntdLeite} litros de leite')
        if gelada.qntdLeite < 10:
            print(f'{familiar} esta comprando mais!')
            gelada.adicionaLeite()
        geladaObj.release()


bebendoLeite = Thread(target = mainBeberLeite)
pai = Thread(target = monitora , args = ('papai',))
mae = Thread(target = monitora , args = ('mamae',))
tio = Thread(target = monitora , args = ('titio',))


bebendoLeite.start()
pai.start()
mae.start()
tio.start()
