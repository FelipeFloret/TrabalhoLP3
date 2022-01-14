class Pilha:
    def __init__(self): #Construtor
        self.__MAX = 1000 #__ Significa private
        self.__Valores =[]
        self.__Topo = -1

    def empty (self):
        return self.__Topo == -1 #Retorna true se estiver vazia

    def push(self, novo):
        if type (novo) is int:
            if self.__Topo < self.__MAX:
                self.__Valores.append(novo)   #Add ao final da lista
                self.__Topo +=  + 1
        elif type (novo) is list: # Verifica o tipo se é lista
            for item in novo:
                if self.__Topo <self.__MAX:
                    self.__Valores.append(item) # Addc cada item da lista
                    self.__Topo += +1

        elif type (novo) is Pilha:      #Verifica se o item é uma pilha
            if self.__Topo + novo.__Topo < self.__MAX:
                for item in novo.__Valores:
                    self.__Valores.append(item)  # Addc cada item da lista
                    self.__Topo += 1

    @property #Função get acessa items privates
    def Valores(self):
        return self.__Valores

    def pop(self):
        if not self.empty(): # Verifica se ta vazio
            self.__Topo -= 1
            return self.__Valores.pop()

    def popqtd(self, qtd):
        i = 0
        while i < qtd and not self.empty():
            self.__Topo -= 1
            self.__Valores.pop()
            i += 1
    def topo(self):
        if not self.empty():
            return self.__Valores[self.__Topo]
        else:
            return -1
