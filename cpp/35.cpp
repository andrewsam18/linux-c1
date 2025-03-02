#include<iostream>
using namespace std;
class Batsman{
   protected:
    int runs;
    public:
    void SetRuns(int r){
        runs=r;
    }
};
class Dhoni :public Batsman{
    public: 
    void printRuns(){
        cout <<"Dhoni scored:"<<runs<<endl;
    }
};
class Kohil :public Batsman{
     public: 
    void printRuns(){
        cout <<"kohil scored:"<<runs<<endl;
    }
};
int main(){
Dhoni dhoni;
    Kohil kohil;
    Batsman*batsman1=&dhoni;
     Batsman*batsman2=&kohil;
     batsman1->SetRuns(10);
     batsman2->SetRuns(32);
     dhoni.printRuns();
     kohil.printRuns();
    return 0;
}