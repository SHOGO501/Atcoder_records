#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int N,A;
    cin >> N >> A;
    int amari;
    while (true)
    {
     amari = N % 500;
     N /= 500;
    if(N < 500)break;
    }
    if (A>=amari)cout << "Yes" <<endl;
    else cout << "No" <<endl;
}