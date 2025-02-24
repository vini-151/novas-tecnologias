#include <stdio.h>



int pred(int n){
    return n - 1;
}


int suc(int n){
    return n + 1;
}

int soma(int n1, int n2){

    if(n1 == 0)
        return n2;
    else 
        return soma(pred(n1) , suc(n2));

}

int main(){

    int n1 , n2;

    printf("Digite dois numeros:\n");
    scanf("%d %d", &n1, &n2);

    
    printf("O resultado da soma eh %d", soma(n1, n2));


}