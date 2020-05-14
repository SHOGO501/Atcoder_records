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
    int N,D;
    cin >> N >> D;
    vector<vector<int>> X(N,vector<int>(D));
    for(int i=0;i<N;i++){
    for(int j=0;j<D;j++){
        cin >> X[i][j];
    }
    }
    int ans = 0;
    for(int i=0;i<N;i++){
    for(int j=i+1;j<N;j++){
        int norm = 0;
        for (int k=0;k<D;k++){
        int diff = abs(X[i][k]-X[j][k]);
        norm += diff*diff;
        }
        bool flag = false;
        for(int k=0;k<=norm;k++){
            if(k*k==norm){
            flag = true;
            }
        }
        if(flag)ans++;
    }
    }
    cout << ans << endl;
}