#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll licm(ll a,ll b) { return a/__gcd(a,b)*b;}
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
ll f(ll x, int c,int d){
    ll res = x;
    res -= x/c;
    res -= x/d;
    res += x/licm(c,d);
    return res;
}

int main(){
    ll A,B,C,D;
    cin >> A >> B >> C >>D;
    ll count =  f(B,C,D) - f(A-1,C,D);
    
    cout << count << endl;
}
