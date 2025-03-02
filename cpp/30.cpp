#include<iostream>
#include<string>
using namespace std;
class birthday{
    int day;
    int month;
    int year;
    public:
    birthday(int d,int m,int y){
        day =d;
     month =m;
    year =y;
    }
    void printdob(){
        cout <<day<<"/"<<month<<"/"<<year<<endl;

    }

};
class person{
string name;
birthday bday;
public:
person(string s,birthday b) :name(s),bday(b){


}
void printpersondata(){
    cout<<"name:"<<name<<endl;
    bday.printdob();
}
};
int main(){
birthday b(19,03,1991);
person p("andrews",b);
p.printpersondata();
    return 0;
}