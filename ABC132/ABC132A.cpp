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
    string S;
    cin >> S;
    bool ans = false;
    if(S[0] == S[1] && S[2]==S[3] && S[1] != S[2])ans = true;
    else if(S[0] == S[2] && S[1]==S[3] && S[1] != S[2])ans = true;
    else if(S[0] == S[3] && S[2]==S[1] && S[2] != S[3])ans = true;
if(ans)cout << "Yes" << endl;
else cout << "No" << endl;

}
