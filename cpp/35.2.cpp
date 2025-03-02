#include<iostream>
using namespace std;
class Batsman{//PURE
 public:
  virtual void Specialshot()=0;
    
   
};
class Dhoni :public Batsman{
  public:
 void Specialshot(){
    cout<<"HELICOPTEDshot:"<<endl;
 }
};
class Kohil :public Batsman{
     public:
 void Specialshot(){
    cout<<"COVER DIVE:"<<endl;
 }
};
int main(){
Dhoni dhoni;
    Kohil kohil;
    Batsman*batsman1=&dhoni;
     Batsman*batsman2=&kohil;
     batsman1->Specialshot();
     batsman2->Specialshot();
    return 0;
}