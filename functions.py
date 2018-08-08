def setDir(choice):
    if choice == 1:
        return "cjuridico"
    elif choice == 2:
        return "colam"
    elif choice == 3:
        return "engagement"
    elif choice == 4:
        return "nuestroscursos"
    elif choice == 5:
        return "streaming"
    elif choice == 6:
        return "uvirtual"
    elif choice == 7:
        return "uvirtualevaluaciones"
   

def scanAndWrap(dir,operation,procesos,local,remote):
    if (operation == 'w'):
        dir = "{0}/{0}.txt".format(dir)
        archivo = open(dir,'r+')
    else:
        archivo = open(dir,operation) 
    actualLine = archivo.readline()
    if(actualLine == "procesos\n"):
        while (actualLine != ''):
            actualLine = archivo.readline()
            actualLine = actualLine.replace("\n",'')
            actualLine = actualLine.strip()
            procesos.append(actualLine)
    else:
        print("Error, file in wrong order actual line says {}".format(actualLine))
        archivo.close()
        return None
    actualLine = archivo.readline()
    if(actualLine == "ipslocal\n"):
        while(actualLine != ''):
            actualLine = archivo.readline()
            actualLine = actualLine.replace("\n",'')
            actualLine = actualLine.strip()
            local.append(actualLine)
    else:
        print("Error, file in wrong order actual line says {}".format(actualLine))
        archivo.close()
        return None
    actualLine = archivo.readline()
    if(actualLine == "ipsremote\n"):
        while(actualLine != ''):
            actualLine = archivo.readline()
            actualLine = actualLine.replace("\n",'')
            actualLine = actualLine.strip()
            remote.append(actualLine)
    else:
        print("Error, file in wrong order actual line says {}".format(actualLine))
        archivo.close()
        return None
    archivo.close()
    wrapped = [procesos, [local,remote]]

    return wrapped

def processFound(oldpr,newpr):
    notFound = []
    for process in newpr:
        if (oldpr.count(process) == 0):
            notFound.append(process)
    return notFound

def ipsFound(oldips,newips):
    notFound = []
    print("Locales: {0},Remotas: {1}".format(oldips[0],oldips[1]))
    for local in newips[0]:   
        if(oldips[0].count(local) == 0):
            #print("Primer if {0}, {1}".format(local,newips[1][newips[0].index(local)]))
            notFound.append([local,newips[1][newips[0].index(local)]])

        elif(oldips[1].count(newips[1][newips[0].index(local)]) == 0):
            print("Segundo if {0}, {1}".format(local,newips[1][newips[0].index(local)]))
            notFound.append([local,(newips[1][newips[0].index(local)] + "*")])
    return notFound

def addToFile(dir, pfound, ipsfound):
    dir = "{0}/{0}.txt".format(dir)
    archivo = open(dir,'r+')
    archivo.seek(0,0)
    actualLine = archivo.readline()
    if (actualLine == "procesos\n"):
        while(actualLine != '\n'):
            actualLine = archivo.readline()
    else:
        archivo.close()
    if len(pfound)>0:            
        for p in pfound:
            archivo.write(p)
    actualLine = archivo.readline()
    if (actualLine == "ipslocal\n"):
        while(actualLine != '\n'):
            actualLine= archivo.readline()
    else:
        archivo.close()
    if len(ipsfound):
        for ip in ipsfound:
            archivo.write(ip[0])
    actualLine = archivo.readline()
    if (actualLine == "ipsremote\n"):
        while(actualLine != ''):
            actualLine = archivo.readline()
    else: 
        archivo.close()
    if len(ipsfound):    
        for ip in ipsfound:
            archivo.write(ip[1])    
    archivo.close()                

