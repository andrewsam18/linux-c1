#include <stdio.h>
int main()
{
    /*instead of : void main() we are using int main()*/
    char c;
    int i;
    float f;
    puts("ENTER A CHARCTER:");
    scanf("%c", &c);
    printf("YOU ENTERED %c\n", c);
//	system("cls");
/*instead of:clrscr(); we are using system("cls");or system("clear");*/
puts("ENTER A INTERGER:");
scanf("%i",&i);
printf("YOU ENTERED %i\n",i);
puts("ENTER A FLOAT:");
scanf("%f",&f);
printf("YOU ENTERED %f\n", f);

    return 0;
}
