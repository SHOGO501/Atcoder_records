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
    int N,D,mieru,ans;
    cin >> N >> D;
    mieru = (D * 2) + 1;
    if(N%mieru == 0)ans = (N/mieru);
    else ans = (N/mieru) + 1;
    cout << ans << endl;

}