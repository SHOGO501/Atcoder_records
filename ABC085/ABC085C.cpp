#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n,Y;
    bool ans = false;
    int a,b,c,ans_c;
    cin >> n >> Y;
    for(int x=0;x<=n;x++){
        for(int y=0;y +x<=n;y++){
            c = n - x - y; 
            if(Y == x*10000+y*5000+c*1000 && n==x+y+c){
                ans = true;
                a = x;
                b = y;
                ans_c = c;
                }
            }
        }
    
    if(ans)cout << a << " " << b << " " <<ans_c <<endl;
    else cout << -1 << " " << -1 << " " <<-1 <<endl;
    

}