#include<stdio.h>
#include<pthread.h>
#include<time.h>

void fun1(void *a) {
	time_t t;
	time(&t);
	printf("Current date and time:\n%s\n",ctime(&t));
	pthread_exit(0);
}

int main(){
	pthread_t t1;
	int r;
	r = pthread_create(&t1,NULL,fun1,NULL);
	pthread_join(t1,NULL);
	return 0;
}
