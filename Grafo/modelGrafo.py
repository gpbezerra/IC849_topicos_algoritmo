# primeiro temos que criar a estrutura do gráfico

class Node:
  def __init__(self, node):
    self.id = node # o ID do node atual
    self.adjacent = {} # os nodes adjascente

  def __str__(self):
    return str(self.id) + "os nós adjascentes são: " + str([x.id for x in self.adjacent]) # definimos a função que vai retornar o nó atual e os nós adjascentes

  # aqui adicionamos mais um vizinho ao nó atual
  def add_neighbor(self, neighbor, weight=0):
    self.adjacent[neighbor] = weight
  
  # aqui pegamos as ligações dos nós entre sí, quais nós estão conectados com quais.
  def get_connections(self):
    return self.adjacent.keys()
  
  # pegamos o id do nó
  def get_id(self):
    return self.id
  # aqui pegamos o weight entre os nós ou seja o custo de irmos de um nó para outro
  def get_weight(self, neighbor):
    return self.adjacent[neighbor]

class Graph:
  # função para iniciar o grafo
  def __init__(self):
    self.vert_dict = {}
    self.num_vertices = 0 

  # função que vai iterar sobre todos os vertices do grafo
  def __iter__(self):
    return iter(self.vert_dict.values())
  
  def add_node(self, node):
    self.num_vertices = self.num_vertices + 1 # adicionamos mais um node no contator do número de vertices
    new_node = Node(node) # aqui estamos instânciando um node
    self.vert_dict[node] = new_node
    return new_node