#include<stdio.h>
#include<limits.h>
#include<float.h>
int main(){
    printf("data type\n");
    printf("_____________\n");
    printf("unsigned ranges:\n"); 
    printf("max. char value=%u\n",UCHAR_MAX); 
    printf("max. short int value=%u\n",USHRT_MAX); 
    printf("max. int value=%u\n",UINT_MAX); 
    printf("max. long  value=%lu\n",ULONG_MAX);
    printf("_____________\n");
    printf("\n singed ranges:\n");
    printf("min.char value=%i\n",CHAR_MAX);
    printf("max.char value=%i\n",CHAR_MIN);
    printf("min.short int value%u\n",SHRT_MIN);
printf("max.short int value%u\n",SHRT_MAX);
printf("max.int value%i\n", INT_MAX);
printf("min.int value%i\n", INT_MIN);
printf("min.long int value%li\n", LONG_MIN);
printf("max.long int value%li\n",LONG_MAX);
printf("____________________\n");
printf("\nfloat,double and long double\n");
printf("max. float value =%g\n",FLT_MAX);
printf("min .float value=%g\n ",FLT_MIN);
printf("max. double value=%g\n",DBL_MAX);
printf("min. double value=%g\n",DBL_MIN);
printf("max. long double value=%Lg\n",LDBL_MAX);
printf("min. long double value=%Lg\n",LDBL_MIN);
printf("__________\n");
puts("memory size and datatypes");
printf("char=%libytes\n",sizeof(char));
printf("short int=%libytes\n",sizeof(short));
printf("int=%li bytes\n",sizeof(int));
printf("long int=%libytes\n",sizeof(long));
printf("float=%libytes\n",sizeof(float));
printf("double =%libytes\n",sizeof(double));
return 0;
}
