#Crear mail

print("Crear Mail Generator")

nombre_completo = input("Ingrese su nombre: ")
dominio = input("Ingrese su dominio: ")


def crear_mail(nombre, dominio):
    #Convertir el nombre a minúsculas
    mail_nombre = nombre.lower().strip()  # Eliminar espacios al inicio y al final
    #Reemplazar espacios por puntos
    mail_nombre = mail_nombre.replace(" ", ".")
    #Agregar el dominio
    mail_nombre += "@" + dominio.lower().strip()  # Eliminar espacios al inicio y al final del dominio
    #Reemplazar caracteres especiales
    mail_nombre = mail_nombre.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    mail_nombre = mail_nombre.replace("ñ", "n").replace("ü", "u").replace("ç", "c")
    #Retornar el mail  
    return mail_nombre

print(crear_mail(nombre_completo, dominio))
    

