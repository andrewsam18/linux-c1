#include<stdio.h>
int main(){
    int salary;
    double bonus1 =8.33;
    double bonus2=4;
    puts("your salary");
    scanf("%i",&salary);
    if (salary<10000)
    {
        printf("bonus=%g",salary*bonus1/100);

    }else if (salary<20000)
    {
    printf("bonus=%g",salary*bonus2/100);

    }
    else
    puts("\n no bonus");
    
    return 0;
}