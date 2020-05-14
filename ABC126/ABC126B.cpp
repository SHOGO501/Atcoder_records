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
    int s;
    cin >> s;
    int mae = s/100 ,usiro = s%100;
    if(0<mae && mae<=12 && 0<usiro && usiro<=12 )cout << "AMBIGUOUS" << endl;
    else if(0<mae && mae<=12)cout << "MMYY" << endl;
    else if(0<usiro && usiro<=12)cout << "YYMM" <<endl;
    else cout << "NA" << endl;
}
