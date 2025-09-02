#include <stdio.h>

int main() {
  int num, i, table;

  printf("Enter an integer: ");
  scanf("%d", &num);

  printf("Multiplication table of %d:\n", num);
  for (i = 1; i <= 10; ++i) {
    table = num * i;
    printf("%d * %d = %d\n", num, i, table);
  }

  return 0;
}