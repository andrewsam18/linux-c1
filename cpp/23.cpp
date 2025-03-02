#include<iostream>
using namespace std;
void passbyvalue(int a){
    a=45;
}
void passbyreference(int* a){
*a=45;
}
int main(){
int x=10;
passbyvalue(x);
cout<<x<<endl;
int x1=10;
passbyreference(&x1);
cout<<x1<<endl;
    return 0;
}//1-10(x)
//2-45(a)