#include<iostream>
using namespace std;

template<class T>
class number{
T first;
T second;
public:
number(T a,T b){
first=a;
second=b;

}
T larger(){
    if (first >second)
    {
        return first;
    }
    return second;
    
}
};
//we use this types to give any datatypes like int, double,float
int main(){
  number<int> numbers(5,6);
  cout <<numbers.larger()<<endl;
        return 0;
}

