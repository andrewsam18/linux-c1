#include<iostream>
using namespace std;
int factorial( int number){
    cout<<"step ->"<<number<<endl;
    if(number==1){
        return 1;
    }
    return number*factorial(number-1);

}
int main(){
 /* 1!=1
    5!=5*4!
    4!=4*3*2*1*/
    cout<<factorial(5)<<endl;
    return 0;
}