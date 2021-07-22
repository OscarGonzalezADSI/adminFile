class AdminFile:
    
    def __init__(self, name):
        self.name = name

    def createFile(self):
        myFile = open(self.name,"w")
        myFile.write("")
        myFile.close()

    def getRead(self):
        myFile = open(self.name,"r")
        content = myFile.read()
        myFile.close()
        
        if(content == ""):
            return "void"
        else:
            return content
    
    def setWrite(self,content):
        myFile = open(self.name,"w")
        myFile.write(content)
        myFile.close()
        
    def addWrite(self,content):
        myFile = open(self.name,"a")
        myFile.write("\n"+content)
        myFile.close()

    def getRows(self):
        i=0
        cadena = ""
        registro = {}
        nroRegistro = 0
        content = self.getRead()
        while(len(content) > i):
            if(content[i] == "\n"):
                registro[nroRegistro] = self.getRegistro(cadena)
                nroRegistro = nroRegistro +1
                cadena = ""
            else:
                cadena = cadena + content[i]
            i=i+1
        if(cadena==""):
            return registro
        else:
            registro[len(registro)] = self.getRegistro(cadena)
            return registro
            
    def getRegistro(self,registro):
        i=0
        data={}
        nroData=0
        cadena=""
        while(len(registro)>i):
            if(registro[i]==";"):
                data[nroData]=cadena
                nroData = nroData +1
                cadena=""
            else:
                cadena=cadena+registro[i]
            i=i+1
        if(cadena==""):
            return data
        else:
            data[len(data)] = cadena
            return data

    def toJson(self):
        cadena = str(self.getRows())
        cadenaSalida=""
        i=0
        llavesApertura = 0
        llavesCierre = 0
        while(len(cadena)>i):
            if(cadena[i]=="{"):
                llavesApertura = llavesApertura+1
                cadenaSalida = cadenaSalida + cadena[i]+"\n"+(llavesApertura*"    ")  
            elif(cadena[i]=="}"):
                llavesApertura = llavesApertura-1
                cadenaSalida = cadenaSalida +"\n"+(llavesApertura*"    ")+cadena[i]
            elif(cadena[i]==","):                
                cadenaSalida = cadenaSalida +cadena[i]+"\n"+((llavesApertura*"    ")[:-1])
            else:
                cadenaSalida = cadenaSalida + cadena[i]
            i=i+1
        return cadenaSalida

    def jsonRow(self,row):
        cadena = self.getRead()
        myArray = cadena.split("},\n")[row].split("\'")
        myArray1 = myArray[1].split("\n       ")
        exita={}
        i=1
        n=0
        while(len(myArray)>i):
            exita[n] = myArray[i]
            i=i+2
            n=n+1
        return exita
    
    def fromJsonToCSVRow(self,row):
        i = 0
        cadena = ""
        while(len(self.jsonRow(row)) > i):
            cadena = cadena + self.jsonRow(row)[i]+";"
            i=i+1
        return cadena

    def fromJsonToCSV(self):
        i=0
        exit = ""
        while(len(self.getRead().split("},\n")) > i):
            exit = exit + self.fromJsonToCSVRow(i)+"\n"
            i = i+1
        return exit

    def fromJsonToCSVformal(self):
        cadena = self.getRead()
        campos={}
        datos={}
        cadena=""
        i=0
        while(len(self.getRead().split("},")) > i):
            campo = self.fromJsonToCSVRow(i).split("},")[0].split(";")[:-1]
            
            if(i==0):
                ii=0
                while(len(campo) > ii):
                    cadena = cadena + campo[ii]+";"
                    ii = ii +2
            
                cadena = cadena + "\n"
            
            ii=1
            while(len(campo) > ii):
                cadena = cadena + campo[ii]+";"
                ii = ii +2
            
            cadena = cadena + "\n"
            
            i = i +1
          
        return cadena
        

    def toJsonStringKeysRow(self,row):
        data={}
        i=0
        while(len(self.jsonRow(0))>i):
            data[self.jsonRow(0)[i]] = self.jsonRow(row)[i]
            i=i+1
        return data

    def toJsonStringKeys(self):
        
        array = self.toJson().split("},\n")
      
        campo = {}
        i = 0
        ii = 1
        while(len(array[0].split("\'")) > ii):
            campo[i] = array[0].split("\'")[ii]
            i = i +1
            ii = ii +2
        
        
        registro = {}
        i=0
        while(len(array)-1>i):
            registro[i]={}
            ii = 1
            iii = 0
            while(len(array[0].split("\'")) > ii):
                registro[i][campo[iii]] = array[i+1].split("\'")[ii]
                iii = iii +1
                ii = ii +2
            i=i+1
        
        cadena = str(registro)
        exit = ""
        i=0
        identacion = 0
        while(len(cadena)>i):
            if(cadena[i]=="{"):
                identacion +=1
                exit = exit + cadena[i] + "\n"+(identacion*"    ")
            elif(cadena[i]=="}"):
                identacion -=1
                exit = exit + "\n"+(identacion*"    ")+ cadena[i]
            elif(cadena[i]==","):
                exit = exit + cadena[i] + "\n"+(identacion*"    ")[:-1]
            else:
                exit = exit + cadena[i]
            i=i+1
        
        return exit
        
        
    def toJsonAddJson(self,datosJson):
        
        array = self.toJson().split("},\n")
      
        campo = {}
        i = 0
        ii = 1
        while(len(array[0].split("\'")) > ii):
            campo[i] = array[0].split("\'")[ii]
            i = i +1
            ii = ii +2
        
        
        registro = {}
        i=0
        while(len(array)-1>i):
            registro[i]={}
            ii = 1
            iii = 0
            while(len(array[0].split("\'")) > ii):
                registro[i][campo[iii]] = array[i+1].split("\'")[ii]
                iii = iii +1
                ii = ii +2
            i=i+1
        
        registro[len(registro)]=datosJson
        return registro

    def fromJsonFormalToOperative(self):
        
        archivo = self.getRead()

        campos = {}
        i=0
        ii=1
        iii=0
        while(len(archivo.split("},")[i].split("\'"))>ii):
            campos[iii] = archivo.split("},")[i].split("\'")[ii]
            ii=ii+4
            iii=iii+1

        data={}
        i=0
        while(len(archivo.split("},"))>i):
            ii=3
            iii=0
            data[i]={}
            while(len(archivo.split("},")[i].split("\'"))>ii):
                data[i][campos[iii]] = archivo.split("},")[i].split("\'")[ii]
                ii=ii+4
                iii=iii+1
            i=i+1
            
        return data


    def fromJsonOperativeToFormal(self,regis):
        cadena = str(regis)
        exit = ""
        i=0
        identacion = 0
        while(len(cadena)>i):
            if(cadena[i]=="{"):
                identacion +=1
                exit = exit + cadena[i] + "\n"+(identacion*"    ")
            elif(cadena[i]=="}"):
                identacion -=1
                exit = exit + "\n"+(identacion*"    ")+ cadena[i]
            elif(cadena[i]==","):
                exit = exit + cadena[i] + "\n"+(identacion*"    ")[:-1]
            else:
                exit = exit + cadena[i]
            i=i+1
        
        self.setWrite(exit)








