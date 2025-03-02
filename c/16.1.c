 #include <stdio.h>
 int main (){
  int num1, num2, num3;
  puts("enter 3 numbers");
  scanf("%i%i%i",&num1,&num2,&num3);
  if(num1>num2){
   if(num1>num3){
      printf("%i greater than %i and %i\n",num1,num2,num3);
      }
      else{
         printf("%i greater than%iand%i\n",num3,num1,num2);
      }
  }else if(num2 >num3){
   printf("%i greater than %i and %i\n",num2,num1,num3);
  }else{
   printf("%i greater than %i and%i\n",num3,num1,num2);
   
  }
    return 0;
 }
