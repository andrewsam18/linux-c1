#include<stdio.h>
int main(){
    int bs ; //basic salary
    float da=30;//dearness allowances
    float hra =20;//housing rent allowances
    float ta=10;//
    double gs;
   
    for (int count=0; count<5; count++)
    { 
        puts("enter basic salary");
        scanf("%i",&bs);
        fflush(stdin);
        gs=bs+bs*da/100+bs*hra/100+bs*ta/100;
        printf("gs=%g\n",gs);
        
    }
    
    return 0;
}