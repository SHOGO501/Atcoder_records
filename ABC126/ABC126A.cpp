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
    int N,K;
    cin >> N >> K;
    string s;
    cin >> s;
    if(s[K-1] == 'A')s[K-1] = 'a';
    else if(s[K-1] == 'B')s[K-1] = 'b';
    else if(s[K-1] == 'C')s[K-1] = 'c';

    cout << s << endl;
}
