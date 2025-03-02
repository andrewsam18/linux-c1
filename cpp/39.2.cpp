#include <iostream>
#include<fstream>
using namespace std;
int main(){
    ofstream numberfile("numbers.txt");
int a;
  while (cin>>a)
  {//eof -ctrl+d
    numberfile<<"number:"<<a<<endl;
  }
  
   
    return 0;
}