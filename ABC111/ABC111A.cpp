#include <bits/stdc++.h>
typedef long long ll;
#define REP(i,n) for(int i=0;i<n;i++)
#define ALL(x) (x).begin(),(x).end()
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
    int a,b,c;
    c = n%10;
    if(c == 1)c = 9;
    else if(c == 9)c = 1;  
    n /= 10;
    
    b = n%10;
    if(b == 1)b = 9;
    else if(b == 9)b = 1;
    n /= 10;

    a = n%10;
    if(a == 1)a = 9;
    else if(a == 9)a = 1;

    int ans = a*100 + b* 10 + c;
    cout << ans << endl;  
}
