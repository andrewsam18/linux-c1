#include <iostream>
#include<string>


using namespace std;
int main(){
  
  string s= "hello";//normal
  string s1("sam");
  string s2="apple";//substr
  string s3="king";//swap
string s4="ball";
string s5="abcdabab";//find
cout<<s<<endl;
cout<<s1<<endl;
cout<<s2<<endl;
cout<<s2.substr(0,3)<<endl;
cout<<s3 <<""<<s4  <<endl;
s3.swap(s4);
cout<<s3 <<""<<s4  <<endl;
cout<<s5.find("ab")   <<endl;

cout<<s5.rfind("ab")   <<endl;
    return 0;
}