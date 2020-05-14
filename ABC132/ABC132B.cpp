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
    int N,count = 0;
    cin >> N;
    int p[N];
    for(int i=0;i<N;i++)cin >> p[i];
    for(int i=0;i<N-2;i++){
        if(p[i] > p[i+1] && p[i+1] > p[i+2] || p[i] < p[i+1] && p[i+1] < p[i+2])count++;
    }
    cout << count << endl;
}