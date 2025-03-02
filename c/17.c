#include<stdio.h>
int main()
{
if (1||1){
    puts("1 or 1 results in  true");
}
   if(1||0){
    puts("1 or 1 results in ture");
   } 
   if(0||1){
    puts("0 or results in true");
   }
   if(0||0){
    puts("this won't be executed");
   }
   else{
    puts("0 or 0 results in false");
   }
   return 0;

}