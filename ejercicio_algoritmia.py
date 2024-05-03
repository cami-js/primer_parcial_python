def comparar_cadenas_lexicograficas(cadena1, cadena2):
    #Verificar que las cadenas ingresadas sean strings
    if not isinstance(cadena1, str) or not isinstance(cadena2, str):
        return "Error: la cadena ingresada no es un string"
    
    #Verificar que las cadenas sean del mismo tamaño
    if not len(cadena1) == len(cadena2):
        return "Error: las cadenas no son del mismo tamaño"
    
    #Verificar que cada letra de la cadena 1 esté en el alfabeto
    if not all(letra.isalpha() for letra in cadena1):
        return "Error: la cadena 1 no está compuesta por letras del alfabeto"
    
    #Verificar que cada letra de la cadena 2 esté en el alfabeto
    elif not all(letra.isalpha() for letra in cadena2):
        return "Error: la cadena 2 no está compuesta por letras del alfabeto"
    
    #Comparar las cadenas lexicográficamente
    if cadena1 < cadena2:
        return "-1"
    elif cadena1 > cadena2:
        return "1"
    else:
        return "0"

#Ejemplo de uso:
cadena1 = "abc"
cadena2 = "abd"
resultado = comparar_cadenas_lexicograficas(cadena1, cadena2)
print(resultado)

