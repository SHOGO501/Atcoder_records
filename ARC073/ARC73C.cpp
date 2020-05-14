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
    ll N,T;
    cin >> N>> T;
    ll t[N];
    for(int i=0;i<N;i++)cin >> t[i];
    ll ans;
    for(int i=0;i<N;i++){
        if(t[i+1]-t[i]>T)ans +=T;
        else ans += t[i+1]-t[i];
    }
    cout << ans << endl;
}
