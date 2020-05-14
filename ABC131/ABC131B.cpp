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
    int N,L;
    cin >> N >> L;
    int aji[N],total=0,ans = 0;

    for(int i= 0;i<N;i++){
        aji[i] = L+i;
        total += L + i ;
        }
    int bordor = abs(aji[0]);
    for(int i=1;i<N;i++){
        if(abs(aji[i]) < bordor){
            bordor = abs(aji[i]);
            ans = i;
        }

    }

    cout << total - aji[ans] << endl;
}