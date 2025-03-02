#include <iostream>
using namespace std;
int main(){
    int a =5;
    cout <<&a <<endl;
    int* pointer =  &a;
    cout<<pointer;
    return 0;
}