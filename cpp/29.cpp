#include<iostream>
using namespace std;
class exp{
int a,b;
public:
//exp(int x,int y){
  //a=x;
  //b=y;
exp(int x,int y):a(x),b(y){
}
void printab(){
  cout<<a<<"\n"<<b<<endl;
}
};
int main(){
exp obj(2,3);
obj.printab();
return 0;
}