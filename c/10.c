#include<stdio.h>
int main(){
    int a,b,c;
    puts("enter 2 integer values:");
    scanf("%i %i",&a,&b);
    printf("\nvalue in a =%i\n",a);
	printf("\nvalue in b =%i\n",b);
    c=a;
    a=b;
    b=c;
    puts("\n after swapping..\n");
    printf("value in a=%i\n",a);
    printf("value  in b=%i\n",b);
       return 0;

}