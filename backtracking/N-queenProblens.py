from numpy import matrix
matrix = matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0]]) # criamos então matrizes 4x4
print(matrix) # aqui conseguimos acessar as posições da matriz

global N # N é o número total de rainhas que devemos acessar globalmente em nosso código
N = 4

def printSolution(board):
  for i in range(N):
    for j in range(N):
      if board[i][j] == 1:
        print("Q", end="")
      else:
        print(".", end=" ")
    print()



# Função para checar se a rainha pode ser colocada na coordenada
def isSafe(board, row, col): 
  for i in range(col):
    if board[row][i] == 1:
      return False

  for i, j in zip(range(row, -1,-1),
                  range(col, -1,-1)):
    if board[i][j] == 1:
      return False
    
  for i, j in zip(range(row, N, 1),
                  range(col, -1,-1)):
    if board[i][j] == 1:
      return False
  return True

def solveNQutil(board, col):
#Se todas as rainhas estão colocadas retorna true
  if col >= N:
    return True
  
  # considera uma coluna e tenta colocar a rainhas em todas as linhas uma por uma.
  for i in range(N):
    if isSafe(board, i, col):
      # coloque a rainha no tabuleiro[i][col]
      board[i][col] = 1
      #recorra para colocar os restos das rainhas
      if solveNQutil(board, col + 1) == True:
        return True

      # caso cloocar a rainha no tabuleiro [i][col]
      # não leve a uma solução então 
      board[i][col] = 0 
  # se nenhuma rainha possa ser colocada em nenhuma linha na coluna, retorna falso
  return False


def solveQueen():
  if solveNQutil(matrix, 0) == False:
    print("solution does not exist")
    return False
  printSolution(matrix)
  return True

# driver code
if __name__ == "__main__":
  solveQueen()
  