#include<stdio.h>
int main(){
int bs;//basic salary
int da=30;//dearness allowance
int hra =20;//house rent allowance
int ta=10 ; //travel allowance
int gs;//gross salary
puts("enter basic salary:");
scanf("%i", &bs);
gs=bs+bs*da /100+bs*hra/100+bs*ta/100;
printf("gs%i\n",gs);

return 0;
}