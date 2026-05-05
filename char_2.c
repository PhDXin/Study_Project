#include<stdio.h>
main(void){
	int c;
	int n;
	c =0;
	n =0;
	while ((c=getchar()) != EOF){
		if (c != '\n'){
			n++;
		}
	}
printf("%d\n",n);
}

