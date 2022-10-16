#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cassert>
using namespace std;


void solve(long long N){
    vector<vector<long long> > v;
    v.push_back(vector<long long>());
    v.push_back(vector<long long>(1, 1));
    for(auto i = 2L; i <= N; i++) {
       vector<long long> vv;
       for(auto j : v[i-1]){
         vv.push_back(j);
       } 
       vv.push_back(i);
       for(auto j : v[i-1]) vv.push_back(j);
       v.push_back(vv);
    }
    for(auto i = 0; i < v[N].size(); i++){
        cout << v[N][i];
        if(i != v[N].size() - 1) {
            cout << " ";
        }
    }
    cout << endl;
}

// Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    long long N;
    std::scanf("%lld", &N);
    solve(N);
    return 0;
}