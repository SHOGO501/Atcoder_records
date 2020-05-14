#include <iostream>
#include <algorithm>
using namespace std;

    int main(){
    int n;
    cin >> n;
    int card[n];
    for (int i=0;i<n;i++)cin >> card[i];
    stable_sort(card,card+n,greater<int>());
    int ans = 0;
    for (int i = 0;i<n;i++){
        if (i % 2 == 0) ans += card[i];
        else ans -= card[i];
 }
    cout << ans << endl;
}