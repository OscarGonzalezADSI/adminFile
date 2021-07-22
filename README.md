# adminFile
adminFile
# crea el archivo csv
archivo = AdminFile("base.csv")

archivo.createFile()

archivo.setWrite("1;maria;florencia;3225645345;")

archivo.addWrite("2;oscar;gonzalez;3228858439;")

archivo.addWrite("3;manuel;gutierrez;3134563202;")

archivo.addWrite("4;jose;perez;3134563467;")

print(archivo.getRead())

# transforma el archivo csv en Json
archivoCSV = AdminFile("base.csv")

archivoJson = AdminFile("baseJson.json")

contenido = archivoCSV.toJson()

archivoJson.setWrite(contenido)

print(archivoJson.getRead())

#transforma el archivo json en csv

archivoJson3 = AdminFile("baseJson.json")

archivoCSV = AdminFile("base.csv")

contenido = archivoJson3.fromJsonToCSV()

archivoCSV.setWrite(contenido)

print(archivoCSV.getRead())

# archivo de Excel normal con nombres de columnas
archivo1 = AdminFile("archivoExcel.csv")

archivo1.createFile()

archivo1.setWrite("cod;nombre;apellido;celular;ciudad;")

archivo1.addWrite("1;manuel;gutierrez;3134563202;bogota;")

archivo1.addWrite("2;jose;perez;3134563467;medellín;")

archivo1.addWrite("3;martha;gonzalez;3239448578;cali;")

print(archivo1.getRead())

# transforma el archivo csv en Json de llaves
archivoCSV2 = AdminFile("archivoExcel.csv")

archivoJson = AdminFile("archivoJson.json")

contenido = archivoCSV2.toJsonStringKeys()

archivoJson.setWrite(contenido)

print(archivoJson.getRead())

#transforma el archivo json en csv

archivoJson3 = AdminFile("archivoJson.json")

archivoCSV = AdminFile("archivoExcel2.csv")

contenido = archivoJson3.fromJsonToCSVformal()

archivoCSV.setWrite(contenido)

print(archivoCSV.getRead())
