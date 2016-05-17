#include<stdio.h>

int main() {
	int a[5],temp;
	printf("Enter a array to be sorted \n");
	for (int i = 0;i <= 5;i++) {
		scanf("%d",&a[i]);
		}
	for (int i = 0;i <= 5;i++) {
		if(a[i]<a[i+1]) {
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
		}
	}
	printf("The sorted string is: \n ");
	for (int i = 0;i <= 5;i++) {
		printf("%d \n",a[i]);
		}
	return 0;
}
