#include<iostream>
using namespace std;
class exp{
    int a;
    public:
    exp(){
        a=1;
    
    }
    void printa(){
        cout<<"a="<<a<<endl;
        cout<<"this->a"<<this->a<<endl;
         cout<<"(*this).a=" <<(*this).a<<endl;
    }
};

int main (){
exp e;
e.printa();
}