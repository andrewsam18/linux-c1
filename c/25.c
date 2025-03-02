#include<stdio.h>
int main(){
    int is_prime=1;
    for(int i=2;i<=300; i++){
        for(int j=2;j<=i;j++){
            if(i%j==0&&i!=j){
                is_prime=0;
                break;
            }
        }
        if (is_prime)
        {
            printf("%i\n",i);
        }
        is_prime=1;
        

    }
    return 0;
}