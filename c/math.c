#include <stdio.h>
int main()
{
    int result;
    double fraction;
    puts("addition:");
    result = 10 + 20;
    printf("result=%i\n", 10 + 20); // or printf("10 + 20 =%i\n",result);
    printf("_____________________________\n"); 
    puts("subraction:");
    result=result -5;
    printf("30-%i\n",result);
    printf("------------------\n");
    puts("multiplication:");
    result=result*2;
    printf("25*2=%i\n",result);
    printf("______________\n");
    puts("division:");
    result=result/5;
    printf("50/5=%i\n",result);
    result=result/3;
    printf("10/3=%i\n",result);
    result=result/3.0;
    printf("10/3.0=%i\n",result);
    printf("_____________\n");
    fraction=10/3.0;
    puts(" both integer operands results in integer value");
	printf("10 /3 =%i\n",result);
    printf("___________\n");
    puts("single floating point operand results in double value ");
    printf("10 /3.0=%g\n",fraction);
    printf("_____________________________\n");
	puts("modulus:");
    printf("result=%i/n",10 %3);
    	printf("_____________________________\n");
	puts("increment by one:");
    result=result +1;
    printf("1+1=%i\n",result);
    result++ ;
    printf("result++=%i",result);
    result--;
    printf("result=%i\n",result);
     	++result;
	printf("++result =%i\n", result);
	--result;
	printf("--result =%i\n", result);
	    return 0;
}