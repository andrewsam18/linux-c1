#include<iostream>
using namespace std;
int main(){
    int a=5;
    int b[3];
     int* p=&a;
     cout<<p<<endl;
     //using array
     int* p1=&b[0];
     cout<<p1<<endl;
int* p2=&b[1];
cout<<p2<<endl;
int* p3=&b[2];
cout<<p3<<endl;
p1+=2;
p2++;
cout <<p1<<endl;
cout <<p2<<endl;
    return 0;
}