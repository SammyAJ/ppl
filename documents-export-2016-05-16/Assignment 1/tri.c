#include<stdio.h>
#include<math.h>

int main(){
	int a = 0, b = 0, c = 0;
	int x = 0, y = 0, hyp = 0;
	
	printf("Enter the Three Sides\n");
	scanf("%d%d%d", &a, &b, &c);
	
	if(a > b && a > c){
		hyp = a;
		x = b;
		y = c;
	}
	
	else if(b > a && b > c){
		hyp = b;
		x = a;
		y = c;
	}
	
	else{
		hyp = c;
		x = a;
		y = b;
	}
	
	if((hyp * hyp) == (x * x) + (y * y)){
		printf("The given sides form a Right-Angled Triangle\n");
	}
	else{
		printf("The given sides do not form a sides of a Right-Angled Triangle\n");
	}
	
	return 0;
}
