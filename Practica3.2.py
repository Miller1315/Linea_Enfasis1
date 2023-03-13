
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



