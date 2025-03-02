#include<iostream>
using namespace std;
 class shop{
private:
int money;
public:
void addmoney(){
money=money+5;}
int getmoney(){
    return money;
}
};
int main(){
    shop s;
    s.addmoney(); 
    cout<<s.getmoney();
    return 0;
}