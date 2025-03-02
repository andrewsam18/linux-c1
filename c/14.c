#include<stdio.h>
int main(){
    int p1_amount ;
    int p2_amount;
    puts ("p1 amount");
    scanf("%i",&p1_amount);
    puts("p2 amount");
    scanf("%i",&p2_amount); 
        if(p1_amount>p2_amount)
        {
            puts("p1_amount>p2_amount");
    }
    if(p2_amount>p1_amount)
    {
 
       puts("p2_amount>p1_amount");        
    }
    return 0;
    }