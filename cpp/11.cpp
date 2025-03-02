#include <iostream>
using namespace std;
int main (){
 int val ,val1,val2,val3;
 val=5;
 val=val+1;
cout<<"val="<<val<<endl;
val1=10;
val1++;//post increment operator
cout<<"val1++="<<val1<<endl;
val1--;
cout<<"val1--="<<val1<<endl;
val2=20;
++val2;//pre increment operator
cout<<"++val2="<<val2<<endl;
--val2;
cout<<"--val="<<val2<<endl;
val3=35;
val3+=3;//we can use any operator like (+,-,*,/,%)
cout<<"val3="<<val3<<endl;
    return 0;
}