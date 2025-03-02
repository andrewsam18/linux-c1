#include<iostream>
using namespace std;
void printArray(int a[], int sizeOfArray){
for (int i = 0; i < sizeOfArray; i++)//instead of giving value sizeofarray
{
   cout<<a[i]<<"";
}

}
int main(){
   int a[5] ={1,2,3,4,5 };
   int b[7] ={1,2,3,4,5,6,7};

   printArray(a, 5);
   cout << endl;
   printArray(b, 7);
    return 0;
}