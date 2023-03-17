# Real
from prettytable import PrettyTable

tabla_c = PrettyTable()
tabla_a= PrettyTable()
def init():
    while True:
        try:
            factor_s=float(input("Ingrese factor de servicio entre 1 y 3: "))
            while factor_s<1 or factor_s>3:
                factor_s=float(input("Datos incorrectos \nIngrese factor de servicio entre 1 y 3: "))      
            break
        
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número decimal. Inténtalo de nuevo." + "\033[0;m")

    
    while True:
        try:
            caudal=float(input("Ingrese caudal: "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número decimal. Inténtalo de nuevo." + "\033[0;m")

    while True:
        try:
            temp_e=float(input("Ingrese temperatura de entrada: "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número decimal. Inténtalo de nuevo." + "\033[0;m")

    while True:
        try:
            temp_s=float(input("Ingrese temperatura de salida "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número decimal. Inténtalo de nuevo." + "\033[0;m")

    const1=1000
    const2=0.0003069
    tamañoDT=int(caudal*(temp_e-temp_s)*factor_s*const1*const2)
    print("Tamaño del distrito termico es: ",tamañoDT)

    chiller(tamañoDT)

def chiller(tamañodt):
    print("\n Tamaños de chillers Centrífugos y de Absorción 500TR, 750TR, 1000TR \n")
    print("Favor indicar cantidad y lea con detenimiento \n")
    print("__________________________________________________________ \n")

    while True:
        try:
            c500 = int(input("Ingrese cantidad para 500TR centrífugos: "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número entero. Inténtalo de nuevo." + "\033[0;m")

    while True:
        try:
            c750 = int(input("Ingrese cantidad para 750TR centrífugos: "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número entero. Inténtalo de nuevo." + "\033[0;m")

    while True:
        try:
            c1000 = int(input("Ingrese cantidad para 1000TR centrífugos: "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número entero. Inténtalo de nuevo." + "\033[0;m")


    while True:
        try:
            aa500 = int(input("Ingrese cantidad para 500TR Absorción: "))

            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número entero. Inténtalo de nuevo." + "\033[0;m")


    while True:
        try:
            a750 = int(input("Ingrese cantidad para 750TR Absorción: "))

            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número entero. Inténtalo de nuevo." + "\033[0;m")


    while True:
        try:
            a1000 = int(input("Ingrese cantidad para 1000TR Absorción: "))
            break
        except ValueError:
            print("\033[4;31m"+ "El número ingresado no es un número entero. Inténtalo de nuevo." + "\033[0;m")

    total_c=(500*c500)+(750*c750)+(1000*c1000)
    total_a=(500*aa500)+(750*a750)+(1000*a1000)
    total_ch=total_c+total_a

    print("El total de las suma de chiller es: ",total_ch)

    tope_max=int(total_ch+(total_ch*0.5))

    print("El tope maximo es: ",tope_max)

    if(total_ch<=tamañodt):
        print("\n Las tecnologías seleccionadas no suministran el tamaño del DT \n")
        print("__________________________________________________________ \n")
        chiller()
    elif(total_ch>=tope_max):
        print("\n Las tecnologías seleccionadas superan el tope del DT")
        print("__________________________________________________________ \n") 
        chiller()
    else: 
        print(total_c) 
        centrifugos(total_c)
        absorcion(total_a)     

def centrifugos(parametro1):
    # 1000
    rp=parametro1*0.3190995427365	# 319
    g=(parametro1*511.13199046407)/1000	# 511
    c=(parametro1*0.0035174111853)*(1925000/0.88) # 7694337	
    o=c*0.03	# 230830
    	
    capex=parametro1*0.0035174111853 #3,5174111853
    ft=capex*1000000 #3517411
    e=capex*1700000	#597_9
    b=capex*2000000 #7034822

    tabla_c.field_names = ["Energía", "Emisiones", "Capex", "Opex"]

    tabla_c.add_row(["Red publica", rp, 0, 0])
    tabla_c.add_row(["Microturbina a gas", g, c, o])
    tabla_c.add_row(["Solar fotovoltaica", 0, ft, 0])
    tabla_c.add_row(["Energía eóilca", 0, e, 0])
    tabla_c.add_row(["Energía biomasa", 0, b, 0])
    

    
    crearTablas('centri')


def absorcion(parametro2):
    # 1000
    g=(parametro2*511.13199046407)/1000	# 51113199046	
    c=((parametro2 * 0.0035174111853)*(1925000/0.88)) #7.694.336,96784375	
    o=c*0.03 # 230.830		
    
    capex=parametro2*0.0035174111853 # 3,5174111853 
    ft=(capex*1000000)*1.015 #1.015.000.000 	
    b=capex*2000000 # 7.034.822,3706

    tabla_a.field_names = ["Energía", "Emisiones", "Capex", "Opex"]

    tabla_a.add_row(["Microturbina a gas", g, c, o])
    tabla_a.add_row(["Solar termica", 0, capex, 0])
    tabla_a.add_row(["Energía biomasa", 0, b, 0])
    

    crearTablas('abso')


def crearTablas(resp):
    if resp == 'centri':
        print(tabla_c)	
    elif resp == 'abso':
        print(tabla_a)	

init()
    