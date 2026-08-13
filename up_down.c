#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{

	//1 - 100 사이 난수 생성
	srand(time(NULL));
	int num = rand() % 101;
	
	//유저 변수 선언
	int user;
	
	//맞을 때까지 검사
	while (1)
	{
		printf("Enter a number(1 - 100) : ");
		scanf("%d", &user);

		if (user == num)
		{
			printf("Congratulations. You got it right!!\n");
			break;
		}
		else if (user < num)
		{
			printf("Up\n");
		}
		else
		{
			printf("down\n");
		}
	}
	


	return 0;
}