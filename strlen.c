#include<stdio.h>
int stren(char s[]){
	int i;
	i=0;
	while (s[i] != '\0'){
		i++;
	}
return i;
	
}
int main(){
	int n;
	n=stren("qwe");
	printf("%d\n",n);
	return 0;
}
