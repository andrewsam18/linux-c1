#include <iostream>
using namespace std;
void printtypeandvalue(int a){
    cout<<"integer"<<a<<endl;
}
void printtypeandvalue(float b){
    cout<<"decimal"<<b<<endl;
}
int main(){
    int a=2;
    float b =4.5;
    printtypeandvalue(a);
    printtypeandvalue(b);
    return 0;

}