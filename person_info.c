#include <stdio.h>

int main(void) 
{
char name[30];
printf("name:");
scanf_s("%s", name, sizeof(name));
int age;
printf("age:");
scanf_s("%d", &age);
float weight;
printf("weight:");
scanf_s("%f", &weight);
float height;
printf("height:");
scanf_s("%f", &height);

printf("name : %s\n", name);
printf("age : %d\n", age);
printf("weight : %0.2f\n", weight);
printf("height : %0.2f\n", height);
}