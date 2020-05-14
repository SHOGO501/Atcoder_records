#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <tuple>
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
    int N;
    cin >> N;
    vector<long long> L(N);
    REP(i,N)cin >> L[i];
    sort(L.begin(),L.end());

    ll res = 0;

    REP(i,N){
        for(int j=i+1;j<N;j++){
            int k = lower_bound(L.begin(),L.end(),L[i] + L[j]) -L.begin();
            res += max(k - (j+1),0);
        }
    }
    cout << res << endl;
}
