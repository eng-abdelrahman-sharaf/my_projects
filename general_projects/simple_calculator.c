/* this simple calculator only treat  */

#include <stdio.h>

int main (){
    printf("enter the calculation using (*,/,-,+)\n\
\033[94mlike 5*5\033[0m\n");
    double a ,b, result;
    char operator;
    scanf("%lf" , &a);
    scanf("%c" , &operator);
    scanf("%lf" , &b);

    switch(operator){
        case '+':
            result = a+b;
            break;
        case '-':
            result = a-b;
            break;
        case '*':
            result = a*b;
            break;
        case '/':
            result = a/b;
            break;
        default :
            printf("please use an operand of (* / - +) not anyone else\n");
    }

    printf("%.3lf %c %.3lf=%.3lf\n" ,a , operator, b,  result);

    
}