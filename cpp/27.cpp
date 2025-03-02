#include<iostream>
using namespace std;
class exp{
    public:
    exp(){
        cout<<"constructor"<<endl;
    }
    ~exp(){
        cout<<"deconstructor"<<endl;
    }
};

int main(){
    exp obj;
cout<<"main"<<endl;
    return 0;
}