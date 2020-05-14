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
    int N;
    cin >> N;
    int W[N];
    for(int i=0;i<N;i++)cin >> W[i];
    int sum = 0;
    int dis = 1000000;
    for(int i=0;i<N;i++){
        sum += W[i];
        int a = accumulate(W+i+1,W+N,0);
        if(abs(sum-a) < dis)dis = abs(sum-a);
    }
    cout << dis <<endl;


}
