#include <stdio.h>


int main(){
    int i = 0;
    while_i_lt_10 :
        if (!(i <10))
            goto end_of_while;
        printf("%d\n" , i);
        i++;
        goto while_i_lt_10;
    end_of_while:
        printf("while loop ended\n");
}
