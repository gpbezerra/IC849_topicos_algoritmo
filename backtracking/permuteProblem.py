# as entradas de nossa função é list(o quanto valores cada permutação conterá) ex: list= 1 e s = ["a", "b", "c"]
# teremos como saída nesse caso = ["a", "b", "c"], caso list = 2 seria ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
# ou seja definimos a quantidade de valores em cada permutação em "list" e nossos valores trabalhados em "s"
#https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm

def permute(list, s):
  # caso o número de combinações seja 1, retornamos a própria lista
  if list == 1:
    return s
  else:
  # Caso seja maior que 1, retornamos uma lista, que consiste na soma entre os valores, criando a permutações
    return [
      y + x
      for y in permute(1, s) # aqui chamamos nossa função recursivamente
      for x in permute(list - 1, s) # aqui continuamos a fazer as permutaçòes, porém removemos uma permutação já obtida das possibilidades
                                    # que já tenha sido printado ex: não se deve repetir a combinação (a,a)
    ]
# print(permute(3,["a", "b", "c"]))
print(permute(2, ["a", "b", "c",]))
