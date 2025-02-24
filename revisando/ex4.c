#include <stdio.h>

void torre(int numDiscos, char inicio, char auxiliar, char destino){
    if(numDiscos == 1){
        printf("O disco %d foi de %c para %c\n", numDiscos, inicio, destino);
        return;
    }

    torre(numDiscos - 1, inicio, destino, auxiliar);

    if(numDiscos>=3) printf("O disco %d foi de %c para %c\n", numDiscos - 2, inicio, destino);

    torre(numDiscos-1, destino, auxiliar, inicio);

    printf("O disco %d foi de %c para %c\n", numDiscos - 1, auxiliar, destino);
}



int main(){


    int numDiscos;

    printf("Digite o numero de discos.\n");
    scanf("%d", &numDiscos);

    torre(numDiscos, 'A', 'B', 'C');

}