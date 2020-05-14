#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
<<<<<<< HEAD
=======
#include <tuple>
>>>>>>> 316124b8603967ba1c941f06764cb2c4d1c1d109
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
<<<<<<< HEAD
    int A,B,C,D,E,k;
    cin >> A >> B >> C >> D >> E >> k;
    int key = E-A;
    if(k>=key)cout << "Yay!" << endl;
    else cout << ":(" << endl;
 
=======
    char s;
    cin >> s;
    if(s == 'A')cout << "T" << endl;
    else if(s=='T')cout << 'A' << endl;
    else if(s== 'C')cout << 'G' << endl;
    else cout << 'C' << endl;
>>>>>>> 316124b8603967ba1c941f06764cb2c4d1c1d109
}
