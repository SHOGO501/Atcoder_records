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
    int N,X;
    cin >> N >> X;
    int L[N];
    for(int i=0;i<N;i++)cin >> L[i];
    int ans = 1,D=0;
    for(int i=1;i<=N;i++){
            D = D + L[i-1];
        if(D<=X)ans++;
    }
    cout << ans << endl;
}
