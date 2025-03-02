#include <iostream>
using namespace std;
int x=12;
int main(){
int x=10;
cout<<"1)"<<x <<endl;
cout<<"2)"<<::x <<endl;
    return 0;
}/*we can only use the int value inside curly bracket or write it on top of int main(){} so we can call it anywhere in the program. 
and we write int x=2 in global int x =4 without ::x= global x =main in cout.*/