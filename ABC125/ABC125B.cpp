#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bits/stdc++.h>
typedef long long ll;
#define REP(i,n) for(int i=0;i<n;i++)
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
    int n;
    cin >> n;
    int v[n],c[n];
    REP(i,n)cin >> v[i];
    REP(i,n)cin >> c[i];
    int ans=0;
    REP(i,n){
        if(v[i]>c[i])ans += v[i] - c[i];
    }
    cout << ans << endl;
}
