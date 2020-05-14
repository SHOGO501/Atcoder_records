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

void trace(int A[],int N){
    REP(i,N){
        if(i>0)printf(" ");
        printf("%d",A[i]);
    }
    printf("\n");
}


int main(){
    int A,B,C;
    cin >> A >> B >> C;
    int five=0,seven=0;
    if(A == 5)five++;
    else if(A==7)seven++;
    if(B == 5)five++;
    else if(B==7)seven++;
    if(C == 5)five++;
    else if(C==7)seven++;
    if(five == 2 && seven == 1)puts("YES");
    else puts("NO");
}
