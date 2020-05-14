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
    int n;
    float A[10000];
    cin >> n;
    for(int i=0;i<n;i++)cin >> A[i];
    float ans = 0;
    for(int i=0;i<n;i++)ans += 1/A[i];
    cout << 1/ans << endl;

}