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
    string S;
    cin >> S;
    bool ans = false;
    for(int i=0;i<3;i++){
        if(S[i]== S[i+1])ans = true;
    }
    if(ans)cout << "Bad" << endl;
    else cout << "Good" << endl;
}