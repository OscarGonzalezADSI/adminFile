from adminFile import AdminFile

# crea el archivo .csv
print("\ncreacion del archivo excel.\n")
archivo1 = AdminFile("archivoExcel.csv")
archivo1.createFile()
archivo1.setWrite("cod;nombre;apellido;celular;")
archivo1.addWrite("1;manuel;gutierrez;3134563202;")
archivo1.addWrite("2;jose;perez;3134563467;")
archivo1.addWrite("3;martha;gonzalez;3239448578;")
print(archivo1.getRead())

# transforma el archivo csv a Json 
print("\ntransforma el archivo csv a un Json.\n")
archivoCSV2 = AdminFile("archivoExcel.csv")
archivoJson = AdminFile("archivoJson.json")
contenido = archivoCSV2.toJsonStringKeys()
archivoJson.setWrite(contenido)
print(archivoJson.getRead())

# caso Excel
# toma de nuevos datos por código.
# actualiza la información en el archivo json
# actualiza el archivo de excel
print("\ningrego de nuevos datos por interno.")

campos = "cod;nombre;apellido;celular;"
datos = "1;oscar;Gonzalez;3228858439;"
archivoCSV2.data(campos)
archivoCSV2.setData(datos)

datosJson = archivoCSV2.getDataJson()
datosCSV = archivoCSV2.getDataCSV()

archivoExcel = AdminFile("archivoExcel.csv")
archivoJson = AdminFile("archivoJson.json")

print("actualiza el archivo json.\n")
regis = archivoExcel.toJsonAddJson(datosJson)
archivoJson.fromJsonOperativeToFormal(regis)
print(archivoJson.getRead())

print("\nactualiza el archivo excel .csv\n")
archivoExcel.addWrite(datosCSV)
print(archivoExcel.getRead())

# caso Json
# toma de nuevos datos (por consola, es una opción)
# actualiza la información en el archivo Excel
# actualiza el archivo json

print("\n\n___________\n\n")
print("segun la información presentada en pantalla,")
print("diligencie la toma de datos para ingresar un")
print("nuevo registro\n\n")

campos = "cod;nombre;apellido;celular;"
archivoJson.data(campos)
archivoJson.setDataConsole() # (*)

datosJson = archivoJson.getDataJson()
datosCSV = archivoJson.getDataCSV()
print("\n\n___________\n\n")

archivoJson = AdminFile("archivoJson.json")
archivoExcel = AdminFile("archivoExcel.csv")

print("\n\nactualiza el archivo excel .csv\n\n")
regis = archivoJson.fromJsonToCSVformal() + datosCSV
archivoExcel.setWrite(regis)
print(archivoExcel.getRead())

print("\n\nactualiza el archivo json\n\n")
data = archivoJson.fromJsonFormalToOperative()
data[len(data)]=datosJson
archivoJson.fromJsonOperativeToFormal(data)
print(archivoJson.getRead())

# ------------------------------------------------

# (*) Uso por consola

# Existe la opción de ingresar datos por consola
# mas que todo para labores de desarrollo.
# como se hizo en el caso json.
    
"""
campos = "cod;nombre;apellido;celular;"
archivoJson.data(campos)
archivoJson.setDataConsole()
"""
# ------------------------------------------------
	








