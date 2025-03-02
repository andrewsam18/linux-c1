#include<stdio.h>
int main()
{
   if(1 && 1){
   puts("1 and 1 results true");
   }
   if(1 && 0){
    puts("1 and 0 won't results in true");
    }else
    {
        puts("1 and 0 results in false ");
        }
        if(0 && 1){
          puts("0 and 1 won't results in true");
         puts("0 and 1 results in false");

    }
    if (0 && 0){
        puts("this won't be executed");
        }else{
            puts("0 and 0 results in false");
        }
    
    
    return 0;

}