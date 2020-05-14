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
    int K ,X;
    cin >> K >> X;
    int ans[1000000];
    for(int i=1;i<K*2;i++)ans[i-1] = X - K + i;
    for(int i=0;i<K*2;i++)cout << ans[i] << " ";
    cout << endl;
}