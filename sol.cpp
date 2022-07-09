#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto& e:a){
        cin >> e;
    }
    for (auto it = a.begin(); it != a.end(); it++)
    {
        // Searching the upper bound, i.e., first
        // element greater than *it from beginning
        auto const insertion_point =
                std::upper_bound(a.begin(), it, *it);

        // Shifting the unsorted part
        std::rotate(insertion_point, it, it+1);
    }
    for (int ele:a){
        cout << ele << " ";
    }
}