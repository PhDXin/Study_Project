#include<stdio.h>
main(){
  int n;
  int counter;
  int accumulator;
  n=counter=accumulator=1;
  printf("Please enter an integer:");
  scanf("%d",&n);
  while (counter <= n){
    accumulator=accumulator*counter;
    counter++;
  }
  printf("Factorial :%d\n",accumulator);
}
  
