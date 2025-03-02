#include<stdio.h>
#include<stdlib.h>
int  main(){
    int bs;//basic salary
    float da=30;//dearness allowance
    float hra=20;//house rent allowance
    float ta=10;//travel allowance
    double gs;//gross salary
    char quit='n';
    while (quit!='y')
    {
        puts("enter basic salary");
    
    scanf("%i",&bs);
    fflush(stdin);
    gs=bs+bs*da/100+bs*hra/100+bs*ta/100;
    printf("gs=%g\n",gs);
puts("Quit?(Y)ES/(N)O");
   quit=getchar();
      }  
      return 0;
}