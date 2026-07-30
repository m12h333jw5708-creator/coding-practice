#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int number;

	printf("enter a number : ");
	scanf("%d", &number);

	if (number % 2 == 0)
	{
		printf("even");
	}
	else
	{
		printf("odd");
	}
}