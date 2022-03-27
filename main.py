from cgitb import text


def encriptar(texto):
    print ('Funcion para encriptar texto '+texto)
    textoFinal=''
    for letra in texto:
        textoFinal += letra+'x'
    return textoFinal

def desencriptar(texto):
    print('Funcion para desencriptar '+texto)
    textoFinal=''
    contador=0
    for letra in texto:
        if contador %2 ==0 :         
            textoFinal += letra
        contador +=1
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)
    
    archivo = open(rutaArchivo,'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print ('El archivo se encripto correctamente')


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r')
    texto = archivo.read()
    archivo.close()
    textoDesEncriptado = desencriptar(texto)
    
    archivo = open(rutaArchivo,'w')
    archivo.write(textoDesEncriptado)
    archivo.close()
    print ('El archivo se desencripto correctamente')

    
respuestaEoD = input('Presione E para encriptar o D para desencriptar')
rutaArchivo = input('Ingrese la ruta del archivo')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)