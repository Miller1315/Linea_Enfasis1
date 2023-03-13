
factor_s=float(input("Ingrese factor de servicio entre 1 y 3: "))
while factor_s<1 or factor_s>3:
    factor_s=float(input("Datos incorrectos \nIngrese factor de servicio entre 1 y 3: "))      

caudal=float(input("Ingrese caudal: "))
temp_e=float(input("Ingrese temperatura de entrada: "))
temp_s=float(input("Ingrese temperatura de salida "))
                     
const1=1000
const2=0.0003069

# caudal=774
# temp_e= 10
# temp_s=5.5
# factor_s=1.6

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

chiller()


    