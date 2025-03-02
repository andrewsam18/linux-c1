#include<stdio.h>
int main (){
    int age;
     char is_minor;
     puts("ENTER YOUR AGE:");
     scanf("%i",&age);
     if(age>=18){
        is_minor ='n';
     }
     else{
        is_minor ='y';
     }
     printf("entered age is minor age? %c",is_minor);
    return 0;
}