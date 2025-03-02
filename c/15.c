#include<stdio.h>
int main(){
    int salary;
    double bounus=8.33;
    puts("your salary");
    scanf ("%i",&salary);
    if(salary>10000){
        printf("bonus=%g",salary*bounus);

    } else{
        puts("no bonus");
    }
    return 0;
}