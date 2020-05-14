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
    ll N,M;
    cin >> N >> M;
    ll ans = 0;
    if(N>M){
        ans = M/2;
    }
    else{
        if(M>N*2){
            ans += N;
            M = M -  N*2;
            ans += M/4;
        }
        else{
            ans = M/2;
        }
    }
    cout << ans << endl;
}
