#include<iostream>

using namespace std;
class Human{
  private:
  int age;
  public:
  string name;
  protected:
  int height;
};
class Andrews:public Human
{
public:
void printValue()
{
    //cout<<age<<endl;
    cout<<height<<endl;
    cout<<name<<endl;

}
};

int main(){
Andrews andrews;
andrews.printValue()
;    return 0;
}








