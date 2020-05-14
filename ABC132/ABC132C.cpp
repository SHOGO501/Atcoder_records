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
    int d[n];
    for(int i=0;i<n;i++)cin >> d[i];
    sort(d,d+n);
    bool ans=false;
    if(d[(n/2)-1] < d[n/2])ans =true;
    if(ans)cout << d[n/2] - d[(n/2)-1] << endl;
    else cout << 0 << endl;
}
