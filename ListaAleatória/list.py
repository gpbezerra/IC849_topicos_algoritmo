#Gerar uma lista  (vetor) aleatória com o máximo de elementos possíveis que o computador consegue suportar
#Pegar o resultado e armazenar em algum arquivo (pode ser txt)

import os
import random as randomLib # primeiro precisamos importar uma biblioteca para gerar os dados randomicos
import binarytree 

filePath = "./list.txt"
randomList = []

file = open("list.txt", "w")
filesize = os.path.getsize(filePath)

while filesize < 1048:
  randomList.append(randomLib.randrange(1000000000, 100000000000000000000000000000000))
  file.writelines(str(randomList))
  
file.close

print(binarytree.tree(is_perfect=True))

#TODO Usar a função build da biblioteca binary tree para construir uma árvore binária com uma lista


# print(randomList)