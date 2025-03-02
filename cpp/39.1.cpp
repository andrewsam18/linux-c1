#include <iostream>
#include<fstream>
using namespace std;
int main(){
    ofstream andrews("andrews.txt");
    if(andrews.is_open()){
    andrews<<"hi andrews"<<endl;
    }else{
        cout<<"file open error";
    }
    andrews.close();
    return 0;
}