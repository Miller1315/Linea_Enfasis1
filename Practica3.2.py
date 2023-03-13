
factor_s=float(input("Ingrese factor de servicio entre 1 y 3: "))
while factor_s<1 or factor_s>3:
    factor_s=float(input("Ingrese factor de servicio entre 1 y 3: "))      

caudal=float(input("Ingrese caudal: "))
temp_e=float(input("Ingrese temperatura de entrada: "))
temp_s=float(input("Ingrese temperatura de salida "))

                        
const1=1000
const2=0.0003069

caudal=774
temp_e= 10
temp_s=5.5
factor_s=1.6

tamañoDT=caudal*(temp_e-temp_s)*factor_s*const1*const2
print("Tamaño del distrito termico es: ",tamañoDT)

centrifugo_op=int(input("Escoja las opciones que desees: \n"))

c500 = int(input("Ingrese '1' 500TR centrífugos \n Ingrese '2' para 750TR centrífugos\n Ingrese '3' para 1000TR centrífugos \n Ingrese '4' para 500TR Absorción \n Ingrese '5' para 750TR Absorción \n Ingrese '6' para 1000TR Absorción \n "))
print("Ejemplo: Al presionar '3' '4' '1' \n Escoges las opciones 1000TR centrífugos, 500TR Absorción, 500TR centrífugos ")

    
