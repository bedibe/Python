
#volume=0.0
#R=0.0
#altura=0.0


#R=float(input("digite o valor R:"))
#altura=float(input("digite o valor de altura:"))

#volume = 3.14159 *(R*R) *altura

#print(volume)




THT = 0
VHT = 0.0
PC = 0

THT=int(input("total de horas trabalhadas:"))
VHT=float(input("valor da hora trabalhada:"))
PC=int(input("valor descontado:"))




print("valor é:",((THT*VHT) - (PC * (THT*VHT)/100)))