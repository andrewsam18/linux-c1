#include<iostream>
using namespace std;
class shop{
    private:
    int  money;
    public:
    shop(int m){
        money=m;

    }
    void addmoney(){
        money=money+5;
    }int getmoney(){
   return money;
    }
};
int main(){
    shop s(100);
    s.addmoney();
    cout<<s.getmoney();
    return 0;
    
}