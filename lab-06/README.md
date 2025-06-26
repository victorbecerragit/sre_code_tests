
Dada una lista de numeros, mover todas las ocurrencias del numero 0 al final de la lista.

[1,0,3,6,7,0,9,8,0,4,5,2]

#

recorrer la lista de numeros e ir desplazando las ocurrencias del 0 al final de la lista.

Opcion A - 
i=0
largo=length(lista)
bucle i a largo -1

  si i = lista[i]
     lista[i] > agregar_lista[largo + 1]
     lista[i] < remover_lista[i]


Opcion B -

función moverCerosInPlace(lista):
    escribirPos ← 0

    para leerPos desde 0 hasta longitud(lista)-1:
        si lista[leerPos] ≠ 0 entonces
            # intercambia el elemento no-cero a la "frente"
            temp ← lista[escribirPos]
            lista[escribirPos] ← lista[leerPos]
            lista[leerPos] ← temp

            escribirPos ← escribirPos + 1
        fin si
    fin para

    # a partir de escribirPos hasta el final ya están los ceros
    retornar lista
fin función

# Ejemplo de uso
original ← [1,0,3,6,7,0,9,8,0,4,5,2]
moverCerosInPlace(original)
imprimir original  # → [1,3,6,7,9,8,4,5,2,0,0,0]    