#include<stdio.h>

unsigned long int power(unsigned long int n, unsigned long int r);

int main(){
    unsigned long int n, sum = 0, temp, remainder, digits = 0;

    printf("Enter an Integer\n");
    scanf("%ld", &n);

    temp = n;

    while(temp != 0){
        digits++;
        temp = temp / 10;
    }

    temp = n;

    while(temp != 0){
        remainder = temp % 10;
        sum = sum + power(remainder, digits);

        temp = temp / 10;
    }

    if(n == sum){
        printf("The inputted number \" %ld \" is an Armstrong Number\n", n);
    }
    else{
        printf("The inputted number \" %ld \" is not an Armstrong Number\n", n);
    }

    return 0;
}

unsigned long int power(unsigned long int n, unsigned long int r){
    unsigned long int c, p = 1;

    for(c = 1; c <= r; c++)
        p = p * n;

    return p;
}
