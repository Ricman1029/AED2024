def dibujar_lineas():
    superior = "╔══╦══╦══╦══╦══╦══╦══╦══╦══╗"
    
    medio    = "╠══╬══╬══╬══╬══╬══╬══╬══╬══╣"
    
    inferior = "╚══╩══╩══╩══╩══╩══╩══╩══╩══╝"

    return superior, medio, inferior

def mostrar_numero(numero):
    if not numero[1]:
        print("\033[91m", end= "")
        print(f"{numero[0]:2}", end= "")   
    else:
        print("\033[92m", end= "")
        print(f"{numero[0]:2}", end= "")

def escribir_renglon(fila_carton):
    n = 9
    for i in range (n):
        print("║", end="")
        if fila_carton[i] is None:
            print("▓▓", end= "")
        else:
            mostrar_numero(fila_carton[i])        
        print("\033[0m", end= "")
    
    print("\033[0m", end= "")
    print("║")
        
def dibujar_carton(datos_carton):
    superior, medio, inferior = dibujar_lineas()
    n = 9
    print (superior)
    escribir_renglon(datos_carton[0])   
    print (medio)
    escribir_renglon(datos_carton[1])
    print (medio)
    escribir_renglon(datos_carton[2])
    print (inferior)








    
if __name__ == "__main__":
  
    datos_carton= [[None,(13,True),(11,False),(11,False),(11,False),None,(11,True),(11,True),(11,True)],\
    [(11,True),(14,True),None,(11,True),(11,True),(11,True),(11,True),(11,True),(11,True)],\
        [(11,True),(11,True),(11,True),(11,False),(11,True),None,(11,True),None,(11,True)]]
  
    
    dibujar_carton(datos_carton)



