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
    float v[10000];
    cin >> N;
    for (int i=0;i<N;i++)cin>>v[i];
    float count;
    sort(v,v +N);
    count = (v[0] + v[1])/2;
    for(int i=2;i<N;i++){
        count = (count + v[i]) / 2;
    }
    cout << count << endl;
}