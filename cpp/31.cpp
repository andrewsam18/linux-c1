#include<iostream>
using namespace std;
class exp{
   int var;
   public: 
   exp(){
    var=1;
   }
   friend void changevar(exp& e);
    };
void changevar(exp& e){
    e.var =3;
    cout<<e.var<<endl;
}
int main(){
exp obj;
changevar(obj);
    return 0;
}