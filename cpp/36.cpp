#include<iostream>
using namespace std;
template<class T>//Template basic
T add(T a,T b){
    return a+b;
}
//we use this types to give any datatypes like int, double,float
int main(){
    double a=5.5,b=7;
    cout<<add(a,b)<<endl;
        return 0;
}

