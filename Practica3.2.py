from prettytable import PrettyTable

factor_s=float(input("Ingrese factor de servicio entre 1 y 3: "))
while factor_s<1 or factor_s>3:
    factor_s=float(input("Datos incorrectos \nIngrese factor de servicio entre 1 y 3: "))      

caudal=float(input("Ingrese caudal: "))
temp_e=float(input("Ingrese temperatura de entrada: "))
temp_s=float(input("Ingrese temperatura de salida "))
                     
const1=1000
const2=0.0003069
#********************
caudal=774
temp_e= 10
temp_s=5.5
factor_s=1.6
#Resultado 1710 
#********************
tamañoDT=caudal*(temp_e-temp_s)*factor_s*const1*const2
print("Tamaño del distrito termico es: ",tamañoDT)

def chiller():
    print("\n Tamaños de chillers Centrífugos y de Absorción 500TR, 750TR, 1000TR \n")
    print("Favor indicar cantidad y lea con detenimiento \n")
    print("__________________________________________________________ \n")

    c500 = int(input("Ingrese cantidad para 500TR centrífugos: "))
    c750 = int(input("Ingrese cantidad para 750TR centrífugos: "))
    c1000 = int(input("Ingrese cantidad para 1000TR centrífugos: "))
    aa500 = int(input("Ingrese cantidad para 500TR Absorción: "))
    a750 = int(input("Ingrese cantidad para 750TR Absorción: "))
    a1000 = int(input("Ingrese cantidad para 1000TR Absorción: "))

    #********************
    c500 = 2
    c750 = 0
    c1000 =0
    aa500 = 1000
    a750 = 0
    a1000 = 0

    #********************

    total_c=(500*c500)+(750*c750)+(1000*c1000)
    total_a=(500*aa500)+(750*a750)+(1000*a1000)
    total_ch=total_c+total_a

    
    tope_max=total_ch*(total_ch*0.5)

    if(tamañoDT>total_ch):
        print("\n Las tecnologías seleccionadas no suministran el tamaño del DT \n")
        print("__________________________________________________________ \n")
    elif(tamañoDT<tope_max):
        print("\n Las tecnologías seleccionadas superan el tope del DT")
        print("__________________________________________________________ \n") 
        chiller()  
        centrifugos(total_c)
        absorcion(total_a)     

chiller()

###################

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
    crearTablas('centri')

def absorcion(parametro2):
    # 1000
    g=(parametro2*511.13199046407)/1000	# 51113199046	
    c=((parametro2 * 0.0035174111853)*(1925000/0.88)) #7.694.336,96784375	
    o=c*0.03 # 230.830		
  		
    capex=parametro2*0.0035174111853 # 3,5174111853 //No cuadra del todo	
    ft=(capex*1000000)*1.015 #1.015.000.000 //no cuadra		
    b=capex*2000000 # 7.034.822,3706		
    crearTablas('abso')
#*********************


tabla_c = PrettyTable()
tabla_a= PrettyTable()

# Definir las columnas de la tabla
tabla_c.field_names = ["Energía", "Emisiones", "Capex", "Opex"]
tabla_a.field_names = ["Energía", "Emisiones", "Capex", "Opex"]

# Agregar filas a la tabla
tabla_c.add_row(["Red publica", 25, "Buenos Aires", "Buenos Aires"])
tabla_c.add_row(["Microturbina a gas", 30, "Córdoba", "Buenos Aires"])
tabla_c.add_row(["Solar fotovoltaica", 20, "Rosario", "Buenos Aires"])
tabla_c.add_row(["Energía eóilca", 25, "Buenos Aires", "Buenos Aires"])
tabla_c.add_row(["Energía biomasa", 30, "Córdoba", "Buenos Aires"])
tabla_c.add_row(["Toneladas de refrigeracion", 30, "Córdoba", "Buenos Aires"])

tabla_a.add_row(["Microturbina a gas", 30, "Córdoba", "Buenos Aires"])
tabla_a.add_row(["Solar termica", 20, "Rosario", "Buenos Aires"])
tabla_a.add_row(["Energía biomasa", 30, "Córdoba", "Buenos Aires"])
tabla_a.add_row(["Toneladas de refrigeracion", 30, "Córdoba", "Buenos Aires"])


#*************************

def crearTablas(resp):
    if resp == 'centri':
        print(tabla_c)	
    elif resp == 'abso':
        print(tabla_a)	


    