#include<iostream>
using namespace std;
class exp{
int a;
public:
exp(){
    a=1;
}
void changeA(){
    a=5;
}
 void printA()const{ 
cout<<a <<endl;
}
};
int main(){
exp obj;
obj.printA();
obj.changeA();
obj.printA();
const exp o;
o.printA();
    return 0;
}