#include <stdio.h>

int b;

void funcao_altera_endereco(int **p)
{
	printf("Valor de b = %d\n", b);
	
	*p = &b;
}

int main(void)
{
	int a = 10;
	int *p = &a;

    int **pp = &p;
	
	b = 20;
	
	printf("Endereco ptr = %p\n", p);
	printf("Endereco a = %p, Endereco b = %p\n", &a, &b);
	printf("Valor apontado = %d\n", *p);
	
	funcao_altera_endereco(pp);

	printf("Endereco ptr apos funcao = %p\n", p);
}