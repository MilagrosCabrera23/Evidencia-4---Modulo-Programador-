import time
from esterilizador_uv import EsterilizadorUV

# Verificar que el esterilizador pueda encenderse.
def test_encender():
    esterilizador = EsterilizadorUV()
    assert (esterilizador.encender())

# Verificar que el esterilizador pueda apagarse luego de haber estado prendido.
def test_apagar(): 
     esterilizador = EsterilizadorUV()
     estado = esterilizador.apagar()
     assert(estado == False)

# Verificar que la esterilización inicie después de 2 segundos de haberse encendido el dispositivo.

def test_iniciar_esterilizacion(): 
    esterilizador = EsterilizadorUV() 
    esterilizador.encender()
#     #Testeamos que pasen los dos segundos con metodos de time
    tiempo = time.time()
    estado, ciclos = esterilizador.iniciar_esterilizacion_encendido() 
#     #Testeamos que se encienda correctamente y que haga los ciclos
    assert(estado == True, ciclos == 1 and tiempo <=2 )

#Metodo que testea la cantidad de ciclos que realizo el dispositivo.
def test_len():  
    esterilizador = EsterilizadorUV()  
    cantidad = esterilizador.encender(), esterilizador.iniciar_esterilizacion_encendido()
    assert(len(cantidad))

#Metodo que ajusta la potencia antes de comenzar la esterilizacion, de una potencia entre 10 a 500v. 
def test_ajustar_potencia(): 
    esterilizador = EsterilizadorUV()
    esterilizador.ajustar_potencia(100)
    assert(esterilizador._EsterilizadorUV__potencia == 100)

# Testeamos los metodos getter y str funcionen correctamente: 
def test_get_modo(): 
 esterilizador = EsterilizadorUV(modo="normal") 
 assert(esterilizador.get_modo() == "normal")

def test_get_estado_esterilizacion(): 
     esterilizador = EsterilizadorUV() 
     #comprobamos que cuando esta apagado el estado es False
     assert(esterilizador.get_estado_esterilizacion()== False)
     #comprobamos que al estar encendido,cambia el estado.
     assert( esterilizador.encender(), esterilizador.iniciar_esterilizacion_encendido() == True)

def test_str_metodo(): 
        esterilizador = EsterilizadorUV
        esterilizador._EsterilizadorUV__potencia = 50
        esterilizador._EsterilizadorUV__ciclos_realizados = 2
        resultado = (
            f"Esterilizador UV - ",
            f"Potencia: 50 W,",
            f"Modo: normal ",
            f"Ciclos realizados: 2"
        )
        assert(resultado)

