#include <iostream>
#include <algorithm>
#include <string>
int n;
int a[201];
using namespace std;
int main(){
    
    cin >> n;
    for(int i = 0;i<n;++i)cin >> a[i];
    int ans =0;
    while (true){
    bool exist_odd = false;
    for(int i=0;i<n;i++){
        if (a[i] % 2 != 0) exist_odd = true; 
    }
    if (exist_odd) break;

    for(int i=0;i<n;i++){
        a[i] /= 2;}
    
    ans += 1;

    }
    cout << ans << endl;
} 

