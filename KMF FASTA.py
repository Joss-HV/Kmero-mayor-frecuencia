with open("sequence1_fasta.txt", "r") as fasta:
    linea=fasta.readlines()
Cadena=""

for i in range(1,len(linea)):
    Cadena += linea[1]
Cadena=Cadena.replace("\n", "")
#print(Cadena)

#Cadena="ACGTTGCATGTCGCATGCATGCATGAGAGCT"
K= 3
L=len(Cadena)
Nmax=0

for i in range (L-K+1):
    Kmero=Cadena[i:i+K]
    if Nmax<Cadena.count(Kmero):
        Nmax=Cadena.count(Kmero)
print ("El número máximo de incidencias es: ", Nmax)

resultado= " "
for i in range (L-K+1):
    Kmero=Cadena[i:i+K]
    if Nmax==Cadena.count(Kmero) and resultado.count(Kmero)<1:
        resultado=resultado+ Kmero+ " "
print("Kmero: ",resultado)

