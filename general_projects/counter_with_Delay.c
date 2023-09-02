#include <stdio.h> /* scanf printf */
#include <time.h> /* clock */

void delay (int seconds);

int main()
{
    short num;//counter

    printf("enter count down number : ");
    scanf("%hd" , &num);

    for (int i = num ; i > 0 ; i-- ){
        printf("%d\n" , i);
        delay(1);
    }

    printf("Blast off to the moon!");
}

void delay (int seconds){
    int milliseconds = seconds * 1000;
    int start = clock();
    while (clock() < start + milliseconds);
}