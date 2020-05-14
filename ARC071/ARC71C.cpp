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
    int n;
    cin >> n;
    string s[n];
    for(int i=0;i<n;i++)cin >> s[i];
    string ans;
    for(char c = 'a';c<='z';c++){
        int count = 50000;
        for(int i=0;i<n;i++){
            int counta = 0;
            for(int j=0;j<s[i].size();j++)if(c == s[i][j])counta++;
        count = min(count,counta);
        }
        for(int a=0;a<count;a++)ans += c;
    }
    if(ans.size() > 0)cout << ans << endl;
    else cout << " " << endl;
}
