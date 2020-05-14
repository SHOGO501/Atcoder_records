#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    int moti[10000];
    for (int i;i<n;i++)cin >> moti[i];
    stable_sort(moti,moti + n,greater<int>());
    int ans = 0;
    int key = 101;
    int j;
    for (int i;i<n ;i++){
        j = moti[i];
        if (j < key)ans += 1;

        key = j;
    }
    cout << ans << endl;

}