#include <stdio.h>
#include <math.h>

int main(){

	long num;
 	int div;
	int count = 0;
	
	printf("Digite um numero:\n");
	scanf("%d", &num);

	div = 1;

	while(num/div){
		count++;
		div = pow(10, count);
	}

	printf("numero tem %d digitos", count);


	while(num != 0){
		printf("%ld-", num/(long)pow(10, count-1));
		num = num%(long)pow(10,count-1);
		count--;
	}

}