// prob03.c
// HP Codewars 2005
// Perfect Numbers
//

#include <stdio.h>

int main(int argc, char *argv[]) 
{
	int integer; 
	int x;
	int sum;
	do {
		printf("Enter a positive integer: ");
		scanf("%d",&integer);
		sum = 0;
		if (integer == 0)
			break;
		for (x = 1; x<integer; x++) {
			if (integer%x == 0)
				sum +=x;
		}
		if (sum == integer)
			printf("%d IS perfect\n", integer);
		else
			printf("%d IS NOT perfect\n", integer);
	} while (integer != 0);
	return;
}