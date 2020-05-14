#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    string S;
    cin >> S;
    S.replace(0,3,"2018");
    cout << S << endl;
}