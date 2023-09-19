import numpy as np
import csv

# Gerando um vetor aleatório com 1 milhão de elementos
num_elements = 1000000 
random_vec = np.random.uniform(0, 100, num_elements) # Irá gerar numeros aleatórios no range de 0 - 100

file_name = "random_vector.csv"

# Escrever o vetor no arquivo CSV
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(random_vec)

print(f"Vetor aleatório com {num_elements} elementos armazenado em '{file_name}'.")

# Criando estrutura da árvore binária. 
# OBS: peguei de um site que dava uma estrutura genérica de árvore binária

# Nó
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Árvore
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

# Criando a árvore binária
binary_tree = BinaryTree()

# Inserindo os valores na árvore binária
for value in random_vec:
    binary_tree.insert(value)