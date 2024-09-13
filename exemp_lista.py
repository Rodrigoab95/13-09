def exibir(lista=None):
    for item in lista:
        print(item)

    print("Tamanho = %d \n" %len(lista))

lista = [5, 2, 4, 3]
lista.sort()
lista.insert(0, 1);       #insere o valor 1 na posição 0
lista.reverse()           #inverte os elementos da lista
lista.remove(2)           #remove o elemento 2 da lista
del lista[1]              #remove a posição 1 da lista
exibir(lista)