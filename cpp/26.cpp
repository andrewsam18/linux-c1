#include<iostream>
using namespace std;
class Example
{
public:
void printhello() {
cout <<"hello"<<endl;
}
void printhello1() {
cout <<"hello1"<<endl;}
};
int main(){
//using normal type
    Example object;
    object.printhello();
// using address type
Example object1;
Example*pointer =&object1;
pointer->printhello1();

    return 0;
}