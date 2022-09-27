'''print("olaaaaa ya se python")
print (type(90))
print (type(90.2))
print (type("ola"))
print (type(True))

x=3
print(x*5)
15
print("Cisco"*x)
'CiscoCiscoCisco'

x=3
print("este valor es x:",x)

kevin=["ola","kevin","ahhh", "perrin"]
print (type(kevin))
#<class 'list'>
print(len(kevin))
print(kevin)


lista = [1, 2.5, 'cadena', [5,6] ,4]
print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # cadena
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[1:3]) # [2.5, 'cadena']
print(lista[1:6]) # [2.5, 'cadena', [5, 6], 4]
print("------------------")
for element in lista:   
    print(element)

lista.append(10)
# [1, 2.5, 'cadena', [5,6] , 4, 10]
print(lista)
lista.append([2,5])
# [1, 2.5, 'cadena', [5,6] , 4, 10, [2,5]]

lista.extend([88,99])
# [1, 2.5, 'cadena', [5,6] , 4, 88, 99]

lista=["a","b","c","d","e"]
lista.insert(2,"Z")
print(lista)

lista.remove('cadena') # [1, 2.5, [5,6], 4]
print(lista)

myIndex=lista.index('cadena') # 2
print(myIndex)

myCount = lista.count(7) # 3
print(myCount)

lista = [7, 2.5, 'cadena', 7,[5,6] ,7]

enlace1 = lista
otra_lista = lista.copy()
lista = [5,4,3,2,1]
print(enlace1)
print(otra_lista)


lista.reverse()
print(lista)
# [7, [5, 6], 7, 'cadena', 2.5, 7]
for element in lista:
    print(element)'''

lista = [7,40,10,3,5,60,32]

lista.sort()
print(lista)
# [3, 5, 7, 10, 32, 40, 60]
lista.sort(reverse=True)
# [60, 40, 32, 10, 7, 5, 3]
print(lista)

lista2=["as","ab"]
lista2.sort()
print(lista2)

max(lista) # 60
min(lista) # 3
