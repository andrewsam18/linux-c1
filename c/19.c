#include<stdio.h>
int main(){
    int year;
    puts("ENTER A YEAR:");
scanf("%i",&year);
if(year %4!=0){
    puts("IT IS COMMON YEAR");
}
else if(year % 400 !=0){
    puts("IT IS COMMON YEAR");

}
else{
    puts("IT IS LEAP YEAR");
}

    return 0;

}