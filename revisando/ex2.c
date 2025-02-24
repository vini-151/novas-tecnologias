#include <stdio.h>


int main(){
    int num; 
    int soma = 0;

    printf("Digite um numero:\n");
    scanf("%d", &num);

    for (int i = 0; i < num; i++){
        soma = soma + i*2+1;
    }

    printf("%d", soma);
    

}