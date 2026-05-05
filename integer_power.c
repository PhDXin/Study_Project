#include<stdio.h>
int power(int x,int y){
	int n;
	int accumulator;
	accumulator=1;
	for (n=1;n<=y;n++){
		accumulator = accumulator*x;
	}
return accumulator;
}
int main(){
	printf("%d\n",power(3,3));
	return 0;
}


