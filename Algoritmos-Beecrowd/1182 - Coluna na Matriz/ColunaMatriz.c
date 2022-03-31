#include <stdio.h>
int main()
{
    float matriz[12][12];
    int n = 0;
    int i, j;
    int coluna;
    char op;
    int soma = 0;
    scanf("%d", &coluna);
    scanf("%s",&op);
    
    for(j = 0; j < 12; j++){
        scanf("%f",&matriz[j][coluna]);
        soma += matriz[j][coluna];        
    }
    if(op == 'S'){
        printf("%.1f.1", soma);
    }
    else if (op == 'C'){
        printf("%.1f", soma/12);
    }
    /*
    for(j = 0; j < 12; j++){
        printf("matriz%d][%d]:%f\n", j, coluna, matriz[j][coluna]);
    }
    */
}
/*
   int vendas[5][3];
   int indpro, inddia;

   for(indpro=0; indpro<5; indpro++)  {
      for (inddia=0; inddia<3; inddia++)   {
         printf("\nProduto %d, digite venda do %d dia: ", indpro+1, inddia+1);
         scanf("%d", &vendas[indpro][inddia]);
      }
   }

   printf("\n\nRelação de venda de produtos");

   for(indpro=0; indpro<5; indpro++)   {
      printf("\nProduto %d, 1º dia: %d   2º dia: %d   3º dia: %d", indpro+1, vendas[indpro][0], vendas[indpro][1], vendas[indpro][2]);
   }

   system("PAUSE")
   */