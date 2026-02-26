#2. El Código
#python
def notaMedia(a, b, c):
    return (a + b + c) / 3 
def aprobar(media):
    if media<0 and media>10 :
        print("nota media fuera de rango entre 0 y 10")
    else :
            if media >= 9:
                print("Sobresaliente")
            if media >= 7 and media < 9:
                print("Notable")
            if media >= 5 and media < 7:
                print("Aprobado")
            if media < 5:
                print("Suspenso")
    print("----------------------")

def mostrar(nombre, a, b, c):
    print("Alumno: " + nombre)
    print("Nota 1: " + str(a))
    print("Nota 2: " + str(b))
    print("Nota 3: " + str(c))
    aprobar(notaMedia())
def main():
    mostrar("Ana García", 8, 7, 9)
    mostrar("Luis Pérez", 4, 5, 3)
    mostrar("Marta Gómez", 6, 7, 5)
main()