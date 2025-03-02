#include<stdio.h>
int main (){
    char ch;
    puts("enter a character:\n");
  ch =getchar();
  if(ch>=65 && ch<=90){
    puts ("it is capital letter");
  }
  else if (ch>=97&&ch<=122)
  {
    puts("it is small letter");

  }
  else if(ch>=48 && ch<=57){
    puts("it is a number");
  }
  else{
    puts("it is a symbol");
  }
  printf("entered charater is%c",ch);
    return 0;
}