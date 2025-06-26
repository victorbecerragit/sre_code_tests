def move_zeros_in_place(nums):
    """
    Mueve todos los ceros de la lista `nums` al final, modificando la lista in-place.
    Mantiene el orden relativo de los demás elementos.
    """
    write_pos = 0

    # Recorremos la lista con read_pos
    for read_pos in range(len(nums)):
        if nums[read_pos] != 0:
            # Intercambia el elemento no-cero hacia la posición de escritura
            nums[write_pos], nums[read_pos] = nums[read_pos], nums[write_pos]
            write_pos += 1

    # Al terminar, todos los ceros quedan después de write_pos
    return nums


# Ejemplo de uso
nums = [1,0,3,6,7,0,9,8,0,4,5,2]
print("Lista original:", nums)
# Mover los ceros al final
move_zeros_in_place(nums)
print("Lista modificada:", nums)    