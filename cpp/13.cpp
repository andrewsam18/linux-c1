#include<iostream>
using namespace std;
int main(){
    int age=18;
    bool voting_registred=true; 
   /* if(age>=18){
    if (voting_registred =true){
    cout << "elibgble to vote\n";
    }else{
        cout<<"not eligble to vote\n";
    }
    }else{
        cout <<"not eligble to vote\n";
    }*/
    if (age >=18 && voting_registred==true)
    {
        cout<<"eligble to vote\n";
    }else{
      cout <<"not eligble to vote\n";  
    }
    
   
    return 0;

}