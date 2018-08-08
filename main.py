from functions import *

dirSelect = input("Seleccione el monitoreo a revisar: \n 1. Cjuridico \n 2. Colam \n 3.Engagement \n 4.NuestrosCursos \n 5.Streaming \n 6.Uvirtual \n 7.UvirtualEv \n")

dir = setDir(int(dirSelect))
print(dir)
fileAddress = input("Por favor ingrese la dirección del archivo a comparar: ")

newData = []
oldData = []
newData = scanAndWrap(fileAddress,'r',[],[],[])
oldData = scanAndWrap(dir,'w',[],[],[])

oldProcess = oldData[0]
oldIps = oldData[1]

newProcess = newData[0]
newIps = newData[1]
pFound = []
ipFound = []

pFound = processFound(oldProcess,newProcess)
ipFound =ipsFound(oldIps,newIps)
ipFinal = []
pFinal = []
if (len(pFound) != 0):
    print("Se encontraron los siguientes procesos (1 para añadir, 0 para descartar): ")
    for p in pFound:
        value = input(p+'\n')
        if value == 1:
            pFinal.append(p)
else:
    print("No se encontraron procesos nuevos")

if (len(ipFound) != 0):
    print("Se encontraron las siguientes conexiones (1 para añadir, 0 para descartar): ")
    for ip in ipFound:
        value = input("Local: {0} Remota: {1} \n".format(ip[0],ip[1]))
        if value == 1:
            ipFinal.append(ip)
else:
    print("No se encontraron conexiones nuevas")

addToFile(dir,pFinal,ipFinal)

