#include <stdio.h>
#include<windows.h>
#include <string.h>
#include <stdlib.h>

void main(){
	int numberA, numberB, total;
	char buffer [33];

	printf("Calculate sum of Two numbers.\n");
	printf("Enter Number A  ");
	scanf("%d", &numberA);
	printf("Enter Number B  ");
	scanf("%d", &numberB);
	
	total = numberA + numberB;
	
	itoa (total,buffer,10);

	MessageBox(0, buffer,"Welcome Message",1);
}