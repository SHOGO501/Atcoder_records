#include <iostream>
#include <algorithm>
#include <string>
typedef long long ll;
using namespace std;

int main(){
    int N;
    cin >> N;
    int A[N],B[N+1];
    for(int i=0;i<N;i++){
    cin >> A[i];
    B[A[i]] = i;
    }
    for(int i=1;i<N+1;i++)cout << B[i]+1 << " ";
  
}
