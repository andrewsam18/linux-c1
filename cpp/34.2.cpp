#include<iostream>

using namespace std;
class Human{
 public:
 Human(){
    cout<<"Human constructor"<<endl;
 }
 ~Human(){
    cout<<"Human destructor"<<endl;
 }
};
class Andrews:public Human
{
public:
 Andrews(){
    cout<<"andrews constructor"<<endl;
 }
 ~Andrews(){
    cout<<"andrews destructor"<<endl;
 }

};

int main(){
Andrews andrews;
cout <<"main"<<endl 
;    return 0;
}








