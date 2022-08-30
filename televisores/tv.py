class TV ():
    numTV = 0
    def __init__(self, marca, estado):
        self.__marca = Marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        TV.numTV += 1

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.marca = marca

    def setControl(self,control):
        self.__control = control
    def getControl(self):
        return self.__control
    
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio
    
    def get_volumen(self):
        return self.__volumen
    def set_volumen(self, volumen):
        self.__volumen = volumen

    def get_canal(self):
        return self.__canal
    def set_canal(self, canal):
        self.__canal = canal

    
    def turnOn(self):
        self.__estado = True
    def turnOff(self):
        self.__estado = False
    def canalUp(self):
        self.__canal += 1 if self.__canal<120 and self.__estado==True else 0
    def canalDown(self):
        self.__canal -= 1 if self.__canal>1 and self.__estado==True else 0
    def volumenUp(self):
        self.__volumen += 1 if self.__volumen<7 and self.__estado==True else 0
    def volumenDown(self):
        self.__volumen -= 1 if self.__volumen>1 and self.__estado==True else 0
    

    @classmethod
    def setNumTV(ops,numTV):
        ops.numTV = numTV
    @classmethod
    def getNumTV(ops):
        return ops.numTV