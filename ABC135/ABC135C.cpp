#include <iostream>
#include <algorithm>
#include <string>
typedef long long ll;
using namespace std;

int main(){
    int N;
    cin >> N;
    ll A[N+1],B[N];
    ll count = 0;
    for(int i=0;i<N+1;i++)cin>>A[i];
    for(int i=0;i<N;i++)cin >>B[i];
    for(int i=0;i<N;i++){
      ll left = min(A[i],B[i]);
      count += left;
      B[i] -= left;
      ll right = min(A[i+1],B[i]);
      A[i+1] -= right;
      count += right;


    }
    cout << count << endl;
}
