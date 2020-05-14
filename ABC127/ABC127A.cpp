#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <tuple>
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
    int A,B;
    cin >> A >> B;
    if(A>=13)cout << B << endl;
    else if(A<=5)cout << 0 << endl;
    else cout << B/2 <<endl;
}
