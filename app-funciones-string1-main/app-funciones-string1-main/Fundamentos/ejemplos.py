def mayusculaMinuscula(valor):
    print(valor.upper())
    print(valor.lower())
    print(valor.capitalize())
    print(valor.title())

def longitudMensaje(valor):
    print("La longitud es: ",len(valor))

def convertirNumberString(valor):
    print(str(valor))

def eliminarEspacios(valor):
    print(valor.strip())

def arregloPalabras(valor):
    print(valor.split())

def palabraDeArreglo():
    nombres=["Luis", "Angel", "Maria", "Angelica"]
    print("".join(nombres))