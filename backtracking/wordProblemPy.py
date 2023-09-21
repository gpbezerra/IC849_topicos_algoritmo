# Essa função vai receber 3 entradas, data = a palavra na qual vamos querer permutar, i = por qual index vamos começar a permutação, lenght = o tamanho das permutações

def permute(data, i, lenght):
  if i == lenght: # se já tivermos permutado toda a palavra apenas retornamos o valor da mesma.
    print(data)
  else:
    for j in range(i, lenght): # Aqui criamos um loop que vai do index inicial definido e o lenght que é o tamanho da nossa palavra a ser permutada.
      # aqui fazemos o swap
      data[i], data[j] = data[j], data[i] # trocamos o valor da variável index i pelo valor da variável do loop j 
      permute(data, i + 1, lenght) # aqui chamamos recursivamente nossa função, porém aumentamos o valor do nosso [i]ndex em 1 por cada loop 
      data[i], data[j] = data[j], data[i] # aqui fazemos o swap mais uma vez após primeiro loop 


string = "abc"
n = len(string) # aqui obtemos o tamanho da nossa palavra usando a função len
data = list(string) # Aqui pegamos nossa string, e transformamos ela em uma lista(vetor).
permute(data, 0, n)