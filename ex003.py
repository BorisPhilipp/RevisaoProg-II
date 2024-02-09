""" 
Exercício

Desenvolva a classe Computador e faça as classes Desktop e Notebook
herdarem da classe computador.

    1. Faça um método Sobre para Computador e instancie um Desktop e um
    Notebook. Faça a chamada e observe o comportamento.

    2. Faça um novo método Sobre em Desktop e faça a chamada, observe seu
    comportamento.
    
    3. Faça uma alteração para Notebook herdar de desktop, chame o método
    Sobre e observe o resultado.

    4. Por fim, faça um método Sobre em Notebook, faça a chama e observe. """
class Computador:
    def __init__(self,memoria,cpu,so,marca):
        self.memoria = memoria
        self.cpu = cpu
        self.so = so
        self.marca = marca
    pass

    def Ligar(self):
        print("Pc ligado emoji china john xina")

    def Desligar(self):
        print("Desligado -9999 points")

    def Sobre(self):
        print(f"\n Processador: {self.cpu}\n Memoria RAM: {self.memoria}\n Sistema Operacional: {self.so} \n Marca: {self.marca}")

pc = Computador("16 GB","Intel Core 2 Duo","Fedora"," Mr. I'm High xxDDXZ")

class Desktop(Computador):
    def __init__(self,memoria,cpu,so,marca):
        super().__init__(memoria,cpu,so,marca)

    def sobre(self):
        print("É um Desktop.")

dsk = Desktop("512 MB","Pentium","EndevourOS"," shut up jesser")
dsk.sobre()

class Notebook(Desktop):
    def __init__(self,memoria,cpu,so,marca):
        super().__init__(memoria,cpu,so,marca)

    def sobre(self):
        print("É um Notebook.")

ntb = Notebook("16 GB","Intel Core 2 Duo","Fedora"," Mr. I'm High xxDDXZ")
ntb.sobre()