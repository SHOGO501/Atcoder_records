#include <iostream>
#include <algorithm>
#include <string>
typedef long long ll;
using namespace std;

int main(){
    int  N,K,ans = 0;
  cin >> N >> K;
  int X[N];
    for(int i=0;i<N;i++){
    cin >> X[i];
    if(X[i]>= K)ans++;
    }

    cout << ans << endl;

  
}
