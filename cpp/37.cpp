#include<iostream>
using namespace std;
template<class R>
class value {
public:
value(R a){
        cout<<a<<"is a number"<<endl;
 
}};

template<>
class value <char> {
public:
value(char a){
        cout<<a<<"is a character"<<endl;
 
}};
template<>
class value <double> {
public:
value(double a){
        cout<<a<<"is a double"<<endl;
 
}};
int main(){
value<int>v1(5);
value <char>v2('v'); 
value<double>v3(5.5);
        return 0;
}

