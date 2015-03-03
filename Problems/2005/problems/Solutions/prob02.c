// prob02.c
// HP Codewars 2005
// Reaumur
//

#include <stdio.h>

int main(int argc, char *argv[]) 
{
	float Reaumur; 
	float Fahrenheit;
	printf("Enter Reaumur temperature: ");
	scanf("%f",&Reaumur);
	Fahrenheit = (Reaumur * 2.25) + 32;
	printf("%3.4f degrees Fahrenheit.\n", Fahrenheit);
	return;
}
