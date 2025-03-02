#include<iostream>
using namespace std;
template<class FIRST,class SECOND>//Template basic
FIRST add(FIRST a,SECOND b){
    return a+b;
}
//we use this types to give any datatypes like int, double,float
int main(){
    int a=5;
 double  b=7.5;
    cout<<add(a,b)<<endl;
        return 0;
}

