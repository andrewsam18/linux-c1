#include<iostream>
using namespace std;
class Human{
    public:
    void printName(){
        cout<<"name"<<endl;
    }
};
class Andrews:public Human
{

};

int main(){
Andrews andrews;
andrews.printName();
    return 0;
}








