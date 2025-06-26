
lista = [1, 2, 0, 3, 4,0,  5, 6, 7,0, 8, 9, 10]

def find_first_zero(lst):
    for i, value in enumerate(lst):
        if value == 0:
            lst.append(lst[i])  # Append the zero to the end of the list
            lst.remove(lst[i])  # Remove the zero from its original position
    return lst

if __name__ == "__main__":
    print("Finding the first zero in the list...")
    print(f"Original list: {lista}")
    index = find_first_zero(lista)
    print(f"Modified list: {index}")
     