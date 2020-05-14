#include <set>
#include <map>
#include <list>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <numeric>
#include <complex>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;
    int H[N];
    bool ans = true;
    for(int i=0;i<N;i++)cin >> H[i];
    
    for(int i=0 ;i<N;i++){
        if(H[i]-H[i-1]==1)H[i]= H[i-1];
        else if(H[i] < H[i-1])ans = false;
        else {
            if(H[i] != H[i-1])H[i] = H[i]-1;
        }
            


    }
    if(ans)cout << "Yes" << endl;
    else cout<< "No" << endl;
}