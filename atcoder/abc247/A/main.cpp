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


void solve(std::string S){
  string out(S);
  out[0] = '0';

  for(auto i = 1; i < S.size(); i++) {
      out[i] = S[i-1];
  }
  cout << out << endl;
}

// Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    std::string S;
    std::cin >> S;
    solve(S);
    return 0;
}