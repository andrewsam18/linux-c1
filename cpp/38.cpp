#include<iostream>
using namespace std;
int main(){
int fatherage =50;
int sonage =60;
try{
if (sonage>fatherage)
{
throw -1;//any type abc;
}
}catch(int x){//any data type(...)
cout<<"son age is grather than father" <<"" <<x<<endl;
}

        return 0;
}