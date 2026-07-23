#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double height;
	double weight;

	printf("몸무게(kg)와 키(cm) 입력 : ");
	scanf("%lf %lf", &weight, &height);
	double bmi = weight / ((height / 100) * (height / 100));
	((bmi >= 20.0) && (bmi < 25.0)) ? printf("표준입니다.") : printf("체중 관리가 필요합니다.");

	return 0;
}