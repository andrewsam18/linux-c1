#include <iostream>
#include<fstream>
using namespace std;
int main(){
    ofstream andrews;
    andrews.open("andrews1.txt");
    andrews<<"hi andrews"<<endl;
    andrews.close();
    return 0;
}