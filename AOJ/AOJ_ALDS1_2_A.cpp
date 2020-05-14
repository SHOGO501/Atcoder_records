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
    int N;
    cin >> N;
    int r[N];
    REP(i,N)cin >> r[i];
    int count = 0;
    bool flag = true;
    while (flag){
    flag = false;
    for(int j = N-1;j>=1;j--){
        if(r[j] < r[j-1]){
            int i= r[j];
            r[j] = r[j-1];
            r[j-1] = i;
            flag = true;
            count++;
            }
        }
    }
    trace(r,N);
    cout << count << endl;
}
