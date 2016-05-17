#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
int *tt(void *vargp)
{
  time_t now;
  time(&now);
  printf("%s", ctime(&now));
  return EXIT_SUCCESS;
}
int main()
{
    pthread_t tid;
    printf("Before Thread\n");
    pthread_create(&tid, NULL, tt, NULL);
    pthread_join(tid, NULL);
    printf("After Thread\n");
    exit(0);
}
