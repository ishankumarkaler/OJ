#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto& e:a){
        cin >> e;
    }
    sort(a.rbegin(), a.rend());
    for (int ele:a){
        cout << ele << " ";
    }
}