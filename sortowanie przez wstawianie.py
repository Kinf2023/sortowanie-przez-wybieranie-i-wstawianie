lista_do_posortowania = [5,4,6,8,2,6]
def sortowanie_przez_wstawianie(lista):
    for i in range(len(lista)):
        element = lista[i]
        j = i - 1
        while j >= 0 and element < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = element
        print(lista)

# Przykład użycia

sortowanie_przez_wstawianie(lista_do_posortowania)
print("posortowana lista")
print(lista_do_posortowania)
