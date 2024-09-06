import time

class EsterilizadorUV: 
    def __init__(self, modo="normal"): 
        self.__encendido = False
        self.potencia = 10
        self.__ciclos_realizados = 0    
        self.__modo = modo
        self.__estado_esterilizacion = False

    def encender(self): 
        self.__encendido = True
        return self.__encendido

    def apagar(self):
        self.__encendido = False 
        return self.__encendido 

    def iniciar_esterilizacion_encendido(self): 
        if self.__encendido: 
            time.sleep(2)
            self.__estado_esterilizacion = True 
            self.__ciclos_realizados += 1
            return self.__estado_esterilizacion, self.__ciclos_realizados
        else: 
            raise ValueError("El esterilizador se encuentra apagado.")

   
    def ajustar_potencia(self,nueva_potencia): 
        if 10 <= nueva_potencia <= 500: 
            self.__potencia = nueva_potencia
        else: 
            raise ValueError("El valor de la potencia debe ser desde 10V hasta 500V")

    def __len(self): 
       return  self.__ciclos_realizados

    def get_modo(self): 
        return self.__modo

    def get_estado_esterilizacion(self): 
        return  self.__estado_esterilizacion 

    def __str__(self):
        return (
            f"Esterilizador UV "
            f"Potencia: {self.__potencia} W, "
            f"Modo: {self.__modo}, "
            f"Ciclos realizados: {self.__ciclos_realizados}"
        )

