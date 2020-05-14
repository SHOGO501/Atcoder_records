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
typedef long long ll;

int main(){
    int N;
    ll ans = 0;
    cin >> N;
    map <string,int > score;
    for(int i=0;i<N;i++){
        string s;
        cin >> s;
        sort(s.begin(),s.end());
        score[s]++; 
    }
    for(auto p : score){
        int s = p.second;
        ans += (ll)s*(s-1)/2;
    }
    cout << ans  << endl;
}