#include <stdio.h>
#include <stdlib.h>


int main() {

	int i = 0;
	int num = 0;
	int num1 = 0;
	int num2 = 0;
	while (num % 6 != 5 || num1 % 101 != 100 || num2 % 101 != 100) {

		i++;
		srand(i);
		num = rand();
		num1 = rand();
		num2 = rand();
		//printf("%d\n", num);

	}

	printf("%d", i);

}




