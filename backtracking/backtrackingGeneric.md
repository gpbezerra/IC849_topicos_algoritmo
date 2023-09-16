# código genérico

. buscar a solução usando backtracking recursivo 

void findSolutions(n, other params) :
    if (found a solution) :
        solutionsFound = solutionsFound + 1;
        displaySolution();
        if (solutionsFound >= solutionTarget) : 
            System.exit(0);
        return

    for (val = first to last) :
        if (isValid(val, n)) :
            applyValue(val, n);
            findSolutions(n+1, other params);
            removeValue(val, n);


verificar se a solução existe ou não
  boolean findSolutions(n, other params) :
      if (found a solution) :
          displaySolution();
          return true;

      for (val = first to last) :
          if (isValid(val, n)) :
              applyValue(val, n);
              if (findSolutions(n+1, other params))
                  return true;
              removeValue(val, n);
          return false;

