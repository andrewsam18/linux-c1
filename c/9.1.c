#include<stdio.h>
int main(){
    float c;
    float f;
    puts("enter temperature in fahrenheit");
    scanf("%f",&f);
    c=(f-32)*5/9;
    printf("temperature in celcius=%.2f\n",c);
    return 0;
}