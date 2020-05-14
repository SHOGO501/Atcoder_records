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
    int N;
    cin >> N;
    vector<tuple<string,int,int>>a;
    for(int i=1;i<=N;i++){
        string s;
        int p;
        cin >> s >> p;
        p = p*-1;
        a.push_back(tie(s,p,i));
    }
    sort(a.begin(),a.end());
    for(int i=0;i<N;i++){
        cout << get<2>(a[i]) << endl;
    }


}
