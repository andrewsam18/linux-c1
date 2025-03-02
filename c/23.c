#include<stdio.h>
int main(){
    int month;
    puts("enter a number between 1 to 12");
    scanf("%i",&month);
    for(int days =1;days<=31; days++){
        if ((month==4||month ==6 ||month==9|| month==11)&&days ==31)
			continue;
       printf("days%i/n",days);
       if (month==2&&days==28)break;
       
    }
}