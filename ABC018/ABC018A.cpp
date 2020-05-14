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

int binarysearch(int key,int n,int A[]){
    int left = 0,right = n,mid;
    while(left < right){
        mid = (left + right) / 2;
        if(key == A[mid]) return 1;
        if(key > A[mid])left = mid + 1;
        else right = mid;
    }
    return 0;
}



int main(){
    int A,B,C;
    cin >> A >> B >> C;
    int a=3,b=3,c=3;
    if(B<A)a--;
    if(C<A)a--;
    if(A<B)b--;
    if(C<B)b--;
    if(A<C)c--;
    if(B<C)c--;
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
}