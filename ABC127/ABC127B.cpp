#include <iostream>
#include <algorithm>
#include <string>
typedef long long ll;
using namespace std;





int main(){
    int r,d,x;
    cin >> r >> d >>x;
    int ans = r*x-d;
    cout << ans << endl;
    for(int i=0;i<9;i++){
        ans = r*ans-d;
        cout << ans << endl;
    }
}
