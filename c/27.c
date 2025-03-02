#include<stdio.h>
int  square(int num){
    return num*num;
}
int main(){
    int result;
    result=square(10);
    printf("10*10=%i\n",result);
    return 0;
}