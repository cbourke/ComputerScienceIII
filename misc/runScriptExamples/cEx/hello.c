#include<stdlib.h>
#include<stdio.h>

/**
 * A basic hello world program in C
 */
int main(int argc, char **argv) {

  int i;
  printf("Hello World!\n");
  printf("You passed:\n");

  for(i=0; i<argc; i++) {
    printf("\targv[%2d] = %s\n", i, argv[i]);
  }
  
  return 0;
}
