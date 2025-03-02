#include<iostream>
using namespace std;
int main(){
    int a=5;
    double b=5;
    char ch='a';
    int c[5];
    float d=5;
    int e [5];
    cout<<sizeof(a)<<endl;
     cout<<sizeof(b)<<endl;
    cout<<sizeof(ch)<<endl;
    cout<<sizeof(c)<<endl;
    cout<<sizeof(d)<<endl;
  cout<<sizeof(e[2])<<endl;
    return 0;



}/*bytes=8bits
int -4 bits
double-8bits
char -1bits 
float 4bits
array 20bits
*/
