#include <iostream>
using namespace std;

    int main(){
    int n,a,b,ans = 0;
    cin >> n >> a >> b;
    for (int i=1; i <= n; i++){
        int k = i;
        int sum =0;
        while (k > 0)
        {
            sum += k % 10;
            k /= 10;
        }
        if (sum >= a && sum <= b)ans += i;
    }
    cout << ans << endl;
}