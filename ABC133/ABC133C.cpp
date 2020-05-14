#include <iostream>
#include <algorithm>
#include <string>
typedef long long ll;
using namespace std;

int main(){
    int N;
    cin >> N;
    int A[N],B[N];
    for (int i=0;i<N;i++){
    cin >> A[i];
    B[i] = A[i];
    }
    sort(B,B+N,greater<int>());
    for(int i=0;i<N;i++){
      if (A[i] != B[0])cout << B[0] << endl;
      else cout << B[1] << endl;
    }
}
