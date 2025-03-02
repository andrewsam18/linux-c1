#include<stdio.h>
int main(){
    double bs,gs, bonus =8.33;
    float da =30;
    float hra =20;
    float ta =10;
    int choice;
    do{
        puts("1. calculate gross salary");
	 	puts("2.calcuate bonus");
		 puts("3.quit");
         scanf("%i",&choice);
         fflush(stdin);
         if (choice==3)
         break;{
            puts("enter basic salary:")	;
			  scanf("%1lf",&bs);
         }
         if (choice==1)
         {
            gs =bs+bs*da/100+bs*hra/100+bs*ta/100;
         printf("gross salary=%.2f\n",gs);
         }else if(choice==2){
         if (bs<10000)
         {
            printf("your bonus=%.2f\n", bs*bonus);
         
         }else{
          puts ("you are not allow to get bonus") ;
         }

         
    }
    }while (choice!=3);
 
    
    return 0;


}
