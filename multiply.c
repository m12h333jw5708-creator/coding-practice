#include <stdio.h>

int main(void)
{
    int a;
    int b;
    printf("enter number:");
    scanf_s("%d", &a);
    printf("enter onother number:");
    scanf_s("%d", &b);
    printf("%d * %d = %d", a, b, a * b);
    return 0;
}