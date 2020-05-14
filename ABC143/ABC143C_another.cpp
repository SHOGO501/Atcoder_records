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
    string S;
    cin >> N >> S;

    int res=0;
    for(int i=0;i<N;){
        int j = i;
        while(j<N && S[j] == S[i])j++;
        res++;
        i = j;
    }
    cout << res << endl;
}
