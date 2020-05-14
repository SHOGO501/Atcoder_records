#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
<<<<<<< HEAD:ABC135A.cpp
    int A,B;
    cin >> A >> B;
    if((A + B)%2==0)cout << (A+B)/2 << endl;
    else cout << "IMPOSSIBLE" << endl;
=======
<<<<<<< HEAD
    int N;
    cin >> N;
    int ans,count,key;
    
    for(int i=1;i<=N;i++){
        key = i;
        while (key < 0)
        {
            key /= 10;
            count++;
        }
        if(count %2 != 0)ans++;
        count = 0;
    }
    cout << ans << endl;


=======
    
   int int64_t:;
   int  ret;
  for(int64_t i = 2; i * i <= n; i++) {
    while(n % i == 0) {
      ret[i]++;
      n /= i;
    }
  }
  if(n != 1) ret[n] = 1;
  return ret;
>>>>>>> fc8e59765c7d84df209d4e59c427a48686a8652b

>>>>>>> b0e1b519ba76226038f47c761940fb487305307a:main.cpp
}