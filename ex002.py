class Classe:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    pass

    def introducao(self):
        print(f'Atributo 1 {self.a} Atributo 2 {self.b}')
    
class Computador:
    def __init__(self,memoria,cpu,so):
        self.memoria = memoria
        self.cpu = cpu
        self.so = so
    pass

    def Ligar(self):
        print("Pc ligado emoji china john xina")

    def Desligar(self):
        print("Desligado -9999 points")

    def Sobre(self):
        print(f"\n Processador: {self.cpu}\n Memoria RAM: {self.memoria}\n Sistema Operacional: {self.so}")

pc = Computador("16 GB","Intel Core 2 Duo","Fedora")
pc.Ligar()
pc.Desligar()
pc.Sobre()