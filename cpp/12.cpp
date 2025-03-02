#include<iostream>
using namespace std;
int main(){
    int a=1;
    /*if(a==1){
        cout<<"one\n";
    }else if(a==2){
        cout<<"two\n";
    }else{
        cout<<"other numbers\n";
    }*/
    switch (a)
    {
    case 1:        
     cout<<"one\n";
        break;
    case 2:cout<<"two\n";
    break;
    default:
    cout<<"other numbers\n";
        break;
    }
    return 0;

}