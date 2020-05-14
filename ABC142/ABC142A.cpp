#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    int odd = (N+1)/2;
    double ans = (double)odd/N;
    printf("%.10f\n",ans);

}