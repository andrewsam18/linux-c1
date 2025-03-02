#include <iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
    ifstream numberfile("numbers.txt");
    string s;
int a;
  while (numberfile >> s>>a)
  {//eof -ctrl+d
    cout<<s<<a<<endl;
  }
  
   
    return 0;
}