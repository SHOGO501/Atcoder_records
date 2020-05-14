#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

//素因数分解
vector<pair<ll,int>> factorize(ll n){
    vector<pair<ll,int>>res;
    for(ll i=2;i*i<=n;i++){
        if(n%i)continue;
        res.emplace_back(i,0);
        while (n%i == 0)
        {
        n /= i;
        res.back().second++;
        }
        
    }
    if(n != 1) res.emplace_back(n,1);
    return res;
}

int main(){
    ll W,H,x,y;
    cin >> W >> H >> x >> y;
    int ans = 0;
    double S = (double)(W) * H / 2;
    if (W == 2*x && H == 2*y)ans = 1;

    cout << fixed << setprecision(10) << S << " " << ans << endl;
}
