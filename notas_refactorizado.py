#2. El Código
#python
def calcularNotaMedia(nota1,nota2, nota3):
    return (nota1 + nota2 + nota3) / 3 
def aprobar(nota_media):
    if nota_media<0 or nota_media>10 :
        print("nota media fuera de rango entre 0 y 10")
    else :
            if nota_media >= 9:
                print("Sobresaliente")
            elif nota_media >= 7 :
                print("Notable")
            elif nota_media >= 5 :
                print("Aprobado")
            else :
                print("Suspenso")
    print("----------------------")

def alumnoAprobado(nombre_alumno, nota1, nota2, nota3):
    print("Alumno: " + nombre_alumno)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    media = calcularNotaMedia(nota1, nota2, nota3)
    print("media:"+ media)
    aprobar(media)
def main():
    alumnoAprobado("Ana García", 8, 7, 9)
    alumnoAprobado("Luis Pérez", 4, 5, 3)
    alumnoAprobado("Marta Gómez", 6, 7, 5)
main()