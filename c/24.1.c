#include<stdio.h>
int main(){
    int num;
    long factorial=1;
    puts("enter a number");
    scanf("%i",&num);
    while (num >0)
    {
        factorial*=num--;
        printf("factorial=%li\n",factorial);
    //	printf("factorial=%li",factorial);
	}
    
    return 0;
}
