#include <stdio.h>
#define MAX 5

void backtracking(char v[], int k) {
  char letra;
  if (k == MAX)
  {
    printf("%s\n", v);
  }
  else {
    for (letra = "a"; letra <= "z"; letra++)
    {
      v[k] = letra;
      backtracking(v,k + 1);
    }
  }
}

int main() {
  char v[MAX + 1];
  v[MAX] = "\0";
  backtracking(v, 0) ;

  return 0;
}
